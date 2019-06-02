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

yaw5=[75,77,79,81,83,85,87,89,91,93,95,97,99,101,103,105]
pitch=[1,0,-1,-2,-3,-4,-5,-6,-7]
possible_actions = []
for i in yaw5:
    for j in pitch:
        possible_actions.append((i,j))

def GetMissionXML():
    ''' arena's level is depending on the free moving area of zombie from easy(3x3) medium(5x5) hard(7x7)'''
    return mode.hard

class Shoot(object):
    def __init__(self, alpha = 0.5, gamma=1, n=1):
        """Constructing an RL agent.

        Args
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """
        self.epsilon = 0.5 # chance of taking a random action instead of the best
        self.q_table = {}
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
                    return (round(y['z']),round(y['x']),mz,mx)

    def choose_action(self, s0):
        if s0 not in self.q_table:
            self.q_table[s0] = {}
        for action in possible_actions:
            if action not in self.q_table[s0]:
                self.q_table[s0][action] = -15
        """
        return pitch & angle
        """
        rand = random.uniform(0,1)
        if rand < self.epsilon:
            print("r shot")
            return (random.choice(yaw5),random.choice(pitch))
        else:
            print("q shot")
            angle = max(self.q_table[s0].items(), key=lambda x:x[1])[0]
        return angle

    def act(self, agent_host, angle):
        global life
        self.launch(angle)
        time.sleep(0.3)
        world_state = agent_host.getWorldState()
        for x in world_state.observations:
            for y in json.loads(x.text).get('entities'):
                if "Zombie" in y['name']:
                    target_life = y['life']
                    if life - target_life > 0:
                        print("hit!")
                        return 5
                    else:
                        print("miss!")
                        return -5
        agent_host.sendCommand('quit')
        return 100

    def update_q_table(self, S, A, R):
        self.q_table[S][A] = R
        print("state:",S,"action:",A,"reward:",self.q_table[S][A],"best:",max(self.q_table[S].items(), key=lambda x:x[1])[0])


    def run(self, agent_host):
        """Learns the process to kill the mob in fewest shot. """
        while True:
            s0 = self.get_zombie_state(agent_host)
            a0= self.choose_action(s0)
            r0 = self.act(agent_host, a0)
            if r0 > self.q_table[s0][a0]:
                self.update_q_table(s0,a0,r0)
            if r0 == 100:
                break

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

    num_reps = 30000
    odie = Shoot(n=0)
    for iRepeat in range(num_reps):
        my_mission = MalmoPython.MissionSpec(GetMissionXML(), True)
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
