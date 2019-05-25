---
layout:  default
title:  Status
---

## Video URL:
https://youtu.be/cpCjmsrNa8A

## Project Summary
Train the agent to do the archery. The goal is shoot the target as more accurate as possible.

## Approach
We used Reinforcement learning - Qtable
  Our MDP is that every time our agent shot an arrow, we check the target's (ex: zombie, zombie pigmane) life. If target's life becomes lower, that means agent hit the target. At this moment, we give agent a positive grade(100). If target's life remains the same, we give negative point(-5) to agent.

Reward function is easy to understand. Everytime our agent hit the target, it will receive 100 point. If agent doesn't hit the target, it will receive -5. The purpose of this function is to let our agent knows which angle is good(agent actually hit the target). Some of idea for this function, does we need to make it give different point based on how many shot that agent alreadt shot. We haven't decided we want to make this change or not, but we will keep tracking about it.

The actions that our agent will do in this project are changing it aiming angle and shooting. Basically, our agent will pick a random angle number or get the highest angle value from the Q-table. Then use that angle to shoot. Base on the returning points, we update our Q-table. This process will keep going and collecting more and more shooting data. When more data that agent collect, he will have more oppotunities to hit the target.



## Evaluation
In our project, we offer the agent a policy to distinguish if the arrow hit the target by grade each round. If the agent hit the target, we will reward him with 100 points. If not, we will punish him -5 points. In the agent side, it has a q-table to record all of this information. In the meanwhile, as described above, agent can choose from the random angle(40% probability) or the highest value from the Q-table(60%). If the agent can find a 'hit' angle in the early time, which will be great, because the agent will keep on shooting using that high reward value. However, if we cannot find the angle that can hit the target, the highest value in q-table would be -5 all the time. In this case, 60% chance of looking up q-table to get high value is basically wasted. Therefore, setting  probability of random or q-table could be a headache problem. So far, our best result of finding the best value is at 166th trial.

Sample data from 1-55:
Starting...
angle, reward:  0.38725 -5
angle, reward:  0.60655 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
5 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
10 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.29656 -5
15 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.85687 -5
angle, reward:  0.38725 -5
20 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38947 -5
25 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.77648 -5
30 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.66041 -5
angle, reward:  0.2326 -5
35 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
40 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.59727 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.95011 -5
45 Showing best policy: 0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.27456 -5
angle, reward:  0.4894 -5
angle, reward:  0.38725 -5
angle, reward:  0.50249 -5
50 Showing best policy: 0.38725 -5
angle, reward:  0.6115 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
angle, reward:  0.38725 -5
55 Showing best policy: 0.38725 -5
...
...
...
165 Showing best policy: 0.38725 -5
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.23656 -5
angle, reward:  0.0925 100
angle, reward:  0.0925 100
170 Showing best policy: 0.0925 100
angle, reward:  0.57508 -5
angle, reward:  0.0925 100
angle, reward:  0.84311 -5
angle, reward:  0.0925 100
angle, reward:  0.94159 -5
175 Showing best policy: 0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.21343 -5
angle, reward:  0.0925 100
angle, reward:  0.0925 100
180 Showing best policy: 0.0925 100
angle, reward:  0.83821 -5
angle, reward:  0.30575 -5
angle, reward:  0.91743 -5
angle, reward:  0.0925 100
angle, reward:  0.0925 100
185 Showing best policy: 0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
190 Showing best policy: 0.0925 100
angle, reward:  0.13697 -5
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
angle, reward:  0.0925 100
195 Showing best policy: 0.0925 100

## Remaining Goals and Challenges

<h3>Final Goal</h3>
Our goal for next phase is to shoot a zombie that is moving.


<h3>Challenges<h3>

<h4>Blood info<h4>
First and the biggest challenges we have during the implementation is find the life info of the Zombie(target), since we need it detect if we actually shot Zombie. While exploring the tutoring code, we find that we can actually get that info from <ObservationFromNearbyEntities>.

<h4>Long Distance lead to diverge of arrow</h4>
During the experiment, we found out that if the agent is set too far away from the target, same yaw, same angle can result in a different places. As we search through the website, it is a fact in the Minecraft world. We learned that the arrow will be off its established place.
We have some hard time on what type of methodwe should use to training our agent.

Sample data: 
angle, reward:  0.52537 -5
angle, reward:  0.60934 -5
angle, reward:  0.03893 100
angle, reward:  0.03893 -5
angle, reward:  0.52537 -5
45 Showing best policy: 0.52537 -5


<h4>Make Zombie move continuously<h4>
In the creation mode, Zombie is roughly moving 1 block per 5-10 seconds, which is too slow. However, our goal is to make it move continuously like 1 block per second so that we can have a moving target for us to aim at.

## Resource Used
