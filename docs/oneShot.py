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
from collections import defaultdict
from timeit import default_timer as timer

def GetMissionXML():
    ''' Build an XML mission string that uses the RewardForCollectingItem mission handler.'''

    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                  <About>
                    <Summary>Hello world!</Summary>
                  </About>

                <ServerSection>
                  <ServerInitialConditions>
                    <Time>
                        <StartTime>12800</StartTime>
                        <AllowPassageOfTime>false</AllowPassageOfTime>
                    </Time>
                    <Weather>clear</Weather>
                  </ServerInitialConditions>
                  <ServerHandlers>
                      <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"/>
                      <DrawingDecorator>
                          <DrawCuboid x1="-14" y1="74" z1="-11" x2="17" y2="77" z2="11" type="diamond_block"/>
                          <DrawCuboid x1="-2" y1="74" z1="-11" x2="0" y2="77" z2="11" type="air"/>
                          <DrawCuboid x1="16" y1="77" z1="-10" x2="16" y2="77" z2="10" type="beacon"/>
                          <DrawCuboid x1="2" y1="77" z1="-10" x2="16" y2="77" z2="-10" type="beacon"/>
                          <DrawCuboid x1="2" y1="77" z1="10" x2="16" y2="77" z2="10" type="beacon"/>
                          <DrawCuboid x1="-13" y1="77" z1="-10" x2="-13" y2="77" z2="10" type="beacon"/>
                          <DrawCuboid x1="-13" y1="77" z1="-10" x2="-4" y2="77" z2="-10" type="beacon"/>
                          <DrawCuboid x1="-13" y1="77" z1="10" x2="-4" y2="77" z2="10" type="beacon"/>
                          <DrawCuboid x1="-6" y1="78" z1="-2" x2="-4" y2="80" z2="1" type="glowstone"/>
                          <DrawCuboid x1="-5" y1="78" z1="-1" x2="-4" y2="80" z2="0" type="air"/>
                          <DrawCuboid x1="-3" y1="78" z1="-2" x2="-3" y2="78" z2="1" type="fence"/>
                          <DrawEntity x="-4" y="80" z="0" type="Zombie"/>
                      </DrawingDecorator>
                      <ServerQuitFromTimeUp timeLimitMs="200000"/>
                      <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                  </ServerSection>

                  <AgentSection mode="Creative">
                    <Name>MalmoTutorialBot</Name>
                    <AgentStart>
                        <Placement x="16" y="80" z="0" yaw="90"/>

    				<Inventory>
    					<InventoryItem slot="0" type="bow"/>
    					<InventoryItem slot="1" type="arrow" />
    				</Inventory>

                    </AgentStart>
                    <AgentHandlers>
                      <ObservationFromNearbyEntities>
                           <Range name="entities" xrange="40" yrange="3" zrange="40"/>
                      </ObservationFromNearbyEntities>
                      <ObservationFromFullStats/>
                      <ObservationFromGrid>
                          <Grid name="floor3x3">
                            <min x="-4" y="78" z="-1"/>
                            <max x="-4" y="78" z="-1"/>
                          </Grid>
                      </ObservationFromGrid>
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                      <MissionQuitCommands/>
                      <InventoryCommands/>

                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''

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
        agent_host.sendCommand("pitch -0.1")
        time.sleep(angle)
        agent_host.sendCommand("pitch 0")
        # shoot with full power
        time.sleep(0.1)
        agent_host.sendCommand("use 1")
        time.sleep(1)
        agent_host.sendCommand("use 0")
        time.sleep(0.1)
        # reset angle
        agent_host.sendCommand("pitch 0.1")
        time.sleep(angle)
        agent_host.sendCommand("pitch 0")
        time.sleep(0.5)

    def choose_action(self):
        """
        return angle
        """
        rand = random.uniform(0,1)
        if rand < self.epsilon or len(self.q_table) == 0:
            angle = round(random.uniform(0,1),5)
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
