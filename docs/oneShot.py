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
from collections import defaultdict
from timeit import default_timer as timer




def GetMissionXML():
    ''' arena's level is depending on the free moving area of zombie from easy(3x3) medium(5x5) hard(7x7)'''
    return mode.easy

class Shoot(object):
    def __init__(self, n):
        """Constructing an RL agent.

        Args
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """
        self.epsilon = 0.3 # chance of taking a random action instead of the best
        self.q_table = {}
        self.n = n
        self.alive = True

    def launch(self, angle):
        # set angle
        # shoot with full power
        agent_host.sendCommand("use 1")
        time.sleep(1)
        agent_host.sendCommand("setPitch -"+str(angle))
        agent_host.sendCommand("use 0")

    def choose_action(self):
        """
        return angle
        """
        rand = random.uniform(0,1)
        if rand < self.epsilon or len(self.q_table) == 0:
            angle = random.randint(0,45)
        else:
            angle = max(self.q_table.items(), key=lambda x:x[1])[0]
        return angle

    def act(self, agent_host, angle):
        global target_life
        last_life = target_life
        self.launch(angle)
        world_state = agent_host.getWorldState()
        for x in world_state.observations:
            for y in json.loads(x.text).get('entities'):
                if "Zombie" in y['name']:
                    target_life = y['life']
                    if last_life - target_life > 0:
                        return 100
                    else:
                        return -5
        self.alive = False
        agent_host.sendCommand('quit')
        return 0

    def update_q_table(self, a0, r0):
        self.q_table[a0] = r0

    def run(self, agent_host):
        """Learns the process to compile the best gift for dad. """
        while True:
            a0 = self.choose_action()
            r0 = self.act(agent_host, a0)
            if r0 == 0:
                break
            self.update_q_table(a0, r0)
            print("angle, reward: ", a0, r0)
            time.sleep(0.1)

target_life = 20

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
        target_life = 20
        odie.run(agent_host)
        if (iRepeat + 1) % 5 == 0:
            bestP = max(odie.q_table.items(), key=lambda x:x[1])
            print((iRepeat+1), 'Showing best policy:', bestP[0],bestP[1])
        time.sleep(1)
