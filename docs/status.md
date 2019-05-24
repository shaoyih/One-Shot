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

## Remaining Goals and Challenges
<h3>Goal</h3>
Our goal for next phase is to shoot a zombie that is moving.
<h3>Challenges<h3>
<h4>Blood info<h4>
First and the biggest challenges we have during the implementation is find the life info of the Zombie(target), since we need it detect if we actually shot Zombie. While exploring the tutoring code, we find that we can actually get that info from <ObservationFromNearbyEntities>.
<h4>Make Zombie move continuously<h4>
In the creation mode, Zombie is rough moving 1 block per 5-10 seconds, which is too slow.

## Resource Used
