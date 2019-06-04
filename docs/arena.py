from builtins import range
import random

easy_h='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
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
                          <DrawCuboid x1="-7" y1="78" z1="-2" x2="-4" y2="80" z2="2" type="glowstone"/>
                          <DrawCuboid x1="-6" y1="78" z1="-1" x2="-4" y2="80" z2="1" type="air"/>
                          <DrawCuboid x1="-3" y1="78" z1="-1" x2="-3" y2="78" z2="1" type="fence"/>
                          '''
easy_e = '''</DrawingDecorator>
                      <ServerQuitFromTimeUp timeLimitMs="200000"/>
                      <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                  </ServerSection>
                  <AgentSection mode="Creative">
                    <Name>MalmoTutorialBot</Name>
                    <AgentStart>
                        <Placement x="11" y="80" z="0.5" yaw="90"/>
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
                      <AbsoluteMovementCommands/>
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                      <MissionQuitCommands/>
                      <InventoryCommands/>
                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''


medium_h='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
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
                          <DrawCuboid x1="-9" y1="78" z1="-3" x2="-3" y2="80" z2="3" type="glowstone"/>
                          <DrawCuboid x1="-8" y1="78" z1="-2" x2="-3" y2="80" z2="2" type="air"/>
                          <DrawCuboid x1="-3" y1="78" z1="-2" x2="-3" y2="78" z2="2" type="fence"/>'''
medium_e = '''</DrawingDecorator>
                      <ServerQuitFromTimeUp timeLimitMs="200000"/>
                      <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                  </ServerSection>
                  <AgentSection mode="Creative">
                    <Name>MalmoTutorialBot</Name>
                    <AgentStart>
                        <Placement x="11" y="80" z="0.5" yaw="90"/>
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
                      <AbsoluteMovementCommands/>
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                      <MissionQuitCommands/>
                      <InventoryCommands/>
                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''

hard_h='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
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
                          <DrawCuboid x1="-3" y1="78" z1="-3" x2="-3" y2="78" z2="3" type="fence"/>'''
hard_e='''</DrawingDecorator>
                      <ServerQuitFromTimeUp timeLimitMs="200000"/>
                      <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                  </ServerSection>
                  <AgentSection mode="Creative">
                    <Name>MalmoTutorialBot</Name>
                    <AgentStart>
                        <Placement x="11" y="80" z="0.5" yaw="90"/>
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
                      <AbsoluteMovementCommands/>
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                      <MissionQuitCommands/>
                      <InventoryCommands/>
                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''