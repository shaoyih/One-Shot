---
layout:  default
title:  Status
---

## Project Summary
We are training our agent learning how to shot the arrows. The goal is improve our agent's precision be more accurately.

## Approach
We used Reinforcement learning - Qtable
  Our MDP is that every time our agent shot, we check the target's(ex: zombie, zombie pigmane) life. If target's life is lower than last time we check, that means agent hit the target. At this moment, we give agent a positive point. If target's life still same, we give negative point to agent.

## Evaluation
RL學習是一種強調如何基於環境行動，從而取得最大化的預期利益。在我們的modul中， 我們的射手需要從每一次的射擊中區分出有效射擊與無效射擊，最後進行有效射擊。
## Remaining Goals and Challenges
<h3>Goal</h3>
Our goal for next phase is to shoot a zombie that is moving.
<h3>Challenges<h3>
<h4>Blood info<h4>
First and the biggest challenges we have during the implementation is find the life info of the Zombie(target), since we need it detect if we actually shot Zombie. While exploring the tutoring code, we find that we can actually get that info from <ObservationFromNearbyEntities>.
<h4>Figure out the method<h4>
We have some hard time on what type of methodwe should use to training our agent.
<h4>Make Zombie move continuously<h4>
In the creation mode, Zombie is rough moving 1 block per 5-10 seconds, which is too slow.

## Resource Used
