from __future__ import division
import numpy as np

import MalmoPython
import os
import random
import sys
import time
import json
import random
import math
import errno
import arena as mode
from collections import defaultdict, deque
from timeit import default_timer as timer

h_yaw5=[77,79,81,83,85,87,89,91,93,95,97,99,101,103]
m_yaw5=[81,83,85,87,89,91,93,95,97,99]
e_yaw5=[86,88,90,92,94]
pitch=[0,-1,-2,-3,-4,-5]
act=['shoot','hold']
possible_actions = []
for i in m_yaw5:
    for j in pitch:
        for k in act:
            possible_actions.append((i,j,k))

def GetMissionXML(stri):
    ''' arena's level is depending on the free moving area of zombie from easy(3x3) medium(5x5) hard(7x7)'''
    if stri == 'easy':
        return mode.easy_h+'''<DrawEntity x="'''+str(random.randint(-6,-4)+0.5) + '''" y="80" z="''' + str(random.randint(-1,1)+0.5) + '''" type="Zombie"/>''' + mode.easy_e
    elif stri == 'medium':
        return mode.medium_h + '''<DrawEntity x="''' + str(random.randint(-8,-4)+0.5) + '''" y="80" z="''' + str(random.randint(-2,2)+0.5) + '''" type="Zombie"/>''' + mode.medium_e
    elif stri == 'hard':
        return mode.hard_h + '''<DrawEntity x="''' + str(random.randint(-10,-4)+0.5) + '''" y="80" z="''' + str(random.randint(-3,3)+0.5) + '''" type="Zombie"/>''' + mode.hard_e
    else:
        return 'error'

class Shoot(object):
    def __init__(self, alpha = 0.4, gamma=0.1, n=1):
        """Constructing an RL agent.
        Args
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """
        self.epsilon = 0.8 # chance of taking a random action instead of the best

        # stats part
        
        self.reward=[]
        self.totalCount=0
        self.totalOnTarget=0
        self.shootCount=0
        
        
        self.phasesTemp=0
        self.phasesOnTarget=[]

        self.arrowAngleCount=dict()
        self.arrowAngleOn=dict()
        self.loadStats()

        ##QLearning varaibles
        self.q_table = {}
        self.loadTrainedData()
        self.n, self.alpha, self.gamma = n, alpha, gamma

    def launch(self,angle):
        # set angle
        # shoot with full power
        degrees = 0.0
        agent_host.sendCommand("use 1")
        time.sleep(1)
        agent_host.sendCommand("setYaw "+str(angle[0]))
        agent_host.sendCommand("setPitch "+str(angle[1]))
        time.sleep(0.1)
        agent_host.sendCommand("use 0")
        time.sleep(0.1)

    def get_zombie_state(self,agent_host):
        # wait 0.1 s to be able to fetch the next worldState
        global life
        time.sleep(0.1)
        state = agent_host.getWorldState()
        for x in state.observations:
            for y in json.loads(x.text).get('entities'):
                if "Zombie" in y['name']:
                    mx = 0
                    mz = 0
                    if y['motionX'] < 0: mx = -1
                    elif y['motionX'] > 0: mx = 1
                    if y['motionZ'] < 0: mz = -1
                    elif y['motionZ'] > 0: m = 1
                    life = y['life']
                    return (int(round(y['z'])),int(round(y['x'])),mz,mx)

    def choose_action(self, s0):
        if s0 not in self.q_table:
            self.q_table[s0] = {}
        for action in possible_actions:
            if action not in self.q_table[s0]:
                self.q_table[s0][action] = 0
        """
        return pitch & angle
        """
        rand = random.uniform(0,1)
        if rand < self.epsilon:
            return (random.choice(m_yaw5),random.choice(pitch),random.choice(act))
        else:
            angle = max(self.q_table[s0].items(), key=lambda x:x[1])[0]
        return angle

    def act(self, agent_host, angle):
        global life
        if angle[2] == 'hold':
            return 0
        self.launch(angle)
        time.sleep(0.3)
        world_state = agent_host.getWorldState()
        for x in world_state.observations:
            entities=json.loads(x.text).get('entities')
            if(entities[1]["name"]!="Zombie"):
                return 100-5
            for y in entities:
                if "Zombie" in y['name']:
                    target_life = y['life']
                    if life - target_life > 0:
                        return 20-3
                    else:
                        return -10-5
                
        agent_host.sendCommand('quit')
        

    def update_q_table(self, S, A, R):
        curr_s, curr_a, curr_r = S[0], A[0], R[0]
        G = sum([self.gamma ** i * R[i] for i in range(len(S))])
        old_q = self.q_table[curr_s][curr_a]
        self.q_table[curr_s][curr_a] = old_q + self.alpha * (G - old_q)
        print("state:",curr_s,"action:",curr_a,"reward:",self.q_table[curr_s][curr_a])

    def run(self, agent_host):
        """Learns the process to kill the mob in fewest shot. """
        S, A, R = deque(), deque(), deque()
        shot = 0
        while shot < 5:
            ##update total arrow shot
            self.totalCount+=1

            ##update accuracy number for every 10000 arrows
            if(self.totalCount%10000==0):
                self.phasesOnTarget.append(self.phasesTemp)
                self.phasesTemp=0
            
            
            s0 = self.get_zombie_state(agent_host)
            a0= self.choose_action(s0)
            if a0[2] == 'shoot':
                shot += 1
                self.shootCount+=1
            r0 = self.act(agent_host, a0)
            
            ##update arrow numbers for different angles
            if(a0[2]=='shoot'):
                self.arrowAngleCount[tuple((a0[0],a0[1]))]+=1

            ##update arrow on target quantity
            if(r0>0):
                self.totalOnTarget+=1
                self.phasesTemp+=1

            ## update arrow hit the target on different angles
                if(a0[2]=='shoot'):
                    self.arrowAngleOn[tuple((a0[0],a0[1]))]+=1
                

            ##update reward
            S.append(s0)
            A.append(a0)
            R.append(r0)

            ##update reward list
            self.reward.append(r0)
            print(s0,a0,r0)
        while len(S) >= 1:
            self.update_q_table(S, A, R)
            S.popleft()
            A.popleft()
            R.popleft()
        agent_host.sendCommand('quit')

    

    def loadTrainedData(self):
        path=os.path.dirname(os.path.abspath(__file__))
        if(os.path.isfile(path+"\\"+"qtable.json")):
            with open(path+"\\"+"qtable.json",'r') as file:
                data=json.load(file)
                dicData=json.loads(data)
                key=dicData.keys()
                value=dicData.values()
                k1=[eval(i) for i in key]
                v1=[eval(i) for i in value]
                self.q_table=dict(zip(*[k1,v1]))
        

    def writeData(self):

        with open('qtable.json','w') as outfile:
            key=self.q_table.keys()
            value=self.q_table.values()
            strK=[str(i) for i in key]
            strV=[str(i) for i in value]
            json.dump(json.dumps(dict(zip(*[strK,strV]))),outfile)


    def recordData(self,num):

        with open('qtable'+str(num)+'.json','w') as outfile:
            key=self.q_table.keys()
            value=self.q_table.values()
            strK=[str(i) for i in key]
            strV=[str(i) for i in value]
            json.dump(json.dumps(dict(zip(*[strK,strV]))),outfile)

    def loadStats(self):
        path=os.path.dirname(os.path.abspath(__file__))
        if(os.path.isfile(path+"\\"+"stats.json")):
            with open(path+"\\"+"stats.json",'r') as file:
                tempDict=json.load(file)
                self.reward=tempDict["reward"]
                self.totalCount=tempDict["totalCount"]
                self.totalOnTarget=tempDict["totalOnTarget"]
                self.phasesTemp=tempDict["phasesTemp"]
                self.shootCount=tempDict["shootCount"]
                self.phasesOnTarget=tempDict["phasesOnTarget"]
                self.arrowAngleCount=eval(tempDict["arrowAngleCount"])
                self.arrowAngleOn=eval(tempDict["arrowAngleOn"])
        else:
            self.getArrowAngle()
            
        
    def writeStats(self):
        stats={"reward":self.reward,
                "totalCount":self.totalCount,
                "totalOnTarget":self.totalOnTarget,
               "phasesTemp":self.phasesTemp,
                "phasesOnTarget":self.phasesOnTarget,
                "shootCount":self.shootCount,               
                "arrowAngleCount":str(self.arrowAngleCount),
                "arrowAngleOn":str(self.arrowAngleOn)
               }
        
        with open("stats.json",'w') as OF:
             json.dump(stats, OF)
            
        
            

    def getArrowAngle(self):
        angleDict=dict()
        angleDict2=dict()
        for i in m_yaw5:
            for j in pitch:
                angleDict[tuple((i,j))]=0
                angleDict2[tuple((i,j))]=0
        self.arrowAngleCount=angleDict
        self.arrowAngleOn=angleDict2
                    
        

def main():
    num_reps = 60000
    odie = Shoot(n=0)
    try:
        for iRepeat in range(num_reps):
            ## update
            if(iRepeat%1000==0):
                odie.recordData(iRepeat)
                odie.writeData()
                odie.writeStats()
            my_mission = MalmoPython.MissionSpec(GetMissionXML('medium'), True)
            my_mission_record = MalmoPython.MissionRecordSpec()  # Records nothing by default
            my_mission.setViewpoint(0)
            max_retries = 3
            for retry in range(max_retries):
                try:
                    # Attempt to start the mission:
                    agent_host.startMission(my_mission, my_client_pool, my_mission_record, 0, "Odie")
                    break
                except RuntimeError as e:
                    if retry == max_retries - 1:
                        print("Error starting mission", e)
                        print("Is the game running?")
                        exit(1)
                    else:
                        time.sleep(2)

            world_state = agent_host.getWorldState()
            while not world_state.has_mission_begun:
                time.sleep(0.1)
                world_state = agent_host.getWorldState()

            # Every few iteration Odie will show us the best policy that he learned.
            odie.run(agent_host)
            time.sleep(1)
    except KeyboardInterrupt:
        print("file saved")
        odie.writeData()
        odie.writeStats()
    except:
        print("file saved")
        odie.writeData()
        odie.writeStats()


life = 0
if __name__ == '__main__':
    print('Starting...', flush=True)
    my_client_pool = MalmoPython.ClientPool()
    my_client_pool.add(MalmoPython.ClientInfo("127.0.0.1", 10000))
    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse(sys.argv)
    except RuntimeError as e:
        print('ERROR:', e)
        print(agent_host.getUsage())
        exit(1)
    if agent_host.receivedArgument("help"):
        print(agent_host.getUsage())
        exit(0)

    main()
