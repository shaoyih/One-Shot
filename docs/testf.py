from __future__ import print_function
from __future__ import division
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #4: Challenge - get to the centre of the sponge

from builtins import range
from past.utils import old_div
import MalmoPython
import os
import sys
import time
import json
import random



if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

def Menger(xorg, yorg, zorg, size, blocktype, variant, holetype):
    #draw solid chunk
    genstring = GenCuboidWithVariant(xorg,yorg,zorg,xorg+size-1,yorg+size-1,zorg+size-1,blocktype,variant) + "\n"
    #now remove holes
    unit = size
    while (unit >= 3):
        w=old_div(unit,3)
        for i in range(0, size, unit):
            for j in range(0, size, unit):
                x=xorg+i
                y=yorg+j
                genstring += GenCuboid(x+w,y+w,zorg,(x+2*w)-1,(y+2*w)-1,zorg+size-1,holetype) + "\n"
                y=yorg+i
                z=zorg+j
                genstring += GenCuboid(xorg,y+w,z+w,xorg+size-1, (y+2*w)-1,(z+2*w)-1,holetype) + "\n"
                genstring += GenCuboid(x+w,yorg,z+w,(x+2*w)-1,yorg+size-1,(z+2*w)-1,holetype) + "\n"
        unit = w
    return genstring

def GenCuboid(x1, y1, z1, x2, y2, z2, blocktype):
    return '<DrawCuboid x1="' + str(x1) + '" y1="' + str(y1) + '" z1="' + str(z1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" z2="' + str(z2) + '" type="' + blocktype + '"/>'

def GenCuboidWithVariant(x1, y1, z1, x2, y2, z2, blocktype, variant):
    return '<DrawCuboid x1="' + str(x1) + '" y1="' + str(y1) + '" z1="' + str(z1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" z2="' + str(z2) + '" type="' + blocktype + '" variant="' + variant + '"/>'

x = str(random.randint(-11,-4))
z = str(random.randint(-3,3))


missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
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
                        <DrawCuboid x1="-11" y1="78" z1="-4" x2="-3" y2="80" z2="4" type="glowstone"/>
                        <DrawCuboid x1="-10" y1="78" z1="-3" x2="-3" y2="80" z2="3" type="air"/>
                        <DrawCuboid x1="-3" y1="78" z1="-3" x2="-3" y2="78" z2="3" type="fence"/>
                        <DrawEntity x="''' + x + '''" y="80" z="''' + z + '''" type="Zombie"/>
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="20000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Creative">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x="6" y="80" z="0" yaw="90"/>
                    
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
                  <InventoryCommands/>
                  
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# Create default Malmo objects:
def random_pick_angal():
    rand = random.uniform(0,1)
    return rand
def up_or_down(pick):
    #print(pick)
    '''
    if pick >= 0.5:
        return -1
    if pick < 0.5:
        return 1
    '''
    return -1
def shot():
    agent_host.sendCommand("use 1")
    time.sleep(1)
    agent_host.sendCommand("use 0")
def changing_angal(pick, times):
    if pick < 0:
        agent_host.sendCommand("pitch -0.1")
    else:
        agent_host.sendCommand("pitch 0.1")
    time.sleep(times)
    agent_host.sendCommand("pitch 0")
def reset_angal(pick, times):
    if pick < 0:
        agent_host.sendCommand("pitch 0.1")
    else:
        agent_host.sendCommand("pitch -0.1")
    time.sleep(times)
    agent_host.sendCommand("pitch 0")
def points(target_blood):
    #print("last_life", last_life)
    #print("target_blood = ", target_blood)
    #print("life = ", trace_target_life)
    if target_blood < last_life:
        return 100
    else:
        return -5
agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, False)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission running ", end=' ')

# ADD YOUR CODE HERE
print("x = ",x)
print("z = ",z)
# TO GET YOUR AGENT TO THE DIAMOND BLOCK
target_name = "Zombie"
trace_target_life = 2000
point = 0
last_life = 2000
# Loop until mission ends:
while world_state.is_mission_running:
    last_life = trace_target_life
    time_chose = random_pick_angal()
    #print("angal changing for: ", time_chose, "second")
    #angal_time = up_or_down(time_chose)
    #print(".", end="")
    changing_angal(up_or_down(time_chose),time_chose)
    shot()
    reset_angal(up_or_down(time_chose),time_chose)
    world_state = agent_host.getWorldState()
    for x in world_state.observations:
        #print(json.loads(x.text).get('entities'))
        for y in json.loads(x.text).get('entities'):
            if target_name in y['name']:
                trace_target_life = y['life']
                #print(y)
                print(trace_target_life)
    point += points(trace_target_life)
    print(point)
    for error in world_state.errors:
        print("Error:",error.text)


    
print()
print("Mission ended")
# Mission has ended.
