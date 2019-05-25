---
layout:  default
title:  Status
---

## Project Summary
We are training our agent learning how to shot the arrows. The goal is improve our agent's precision be more accurately.

## Approach
We used Reinforcement learning - Qtable
  Our MDP is that every time our agent shot, we check the target's(ex: zombie, zombie pigmane) life. If target's life is lower than last time we check, that means agent hit the target. At this moment, we give agent a positive point. If target's life still same, we give negative point to agent.

Reward function is easy to understand. Everytime when our agent hit the target, it return 100 point. If agent doesn't hit the target, it will return -5 to agent. The target for this function is according to let our agent knows what kind of shoot is good and should be redo. Some of idea for this function, does we need to make it give different point based on how many shot that agent alreadt shot. We haven't decided we want to make this change or not, but we will keep tracking about it. 

The actions that our agent will do in this project are moving his angle and shoot. 



## Evaluation
RL學習是一種強調如何基於環境行動，從而取得最大化的預期利益。
在我們的modul中， 我們的射手需要從每一次的射擊中區分出有效射擊與無效射擊，最後進行有效射擊。圖表中有顯示reward為100的即為有效射擊，reward為-5的則是無效射擊(這裡放一張分數圖同時有-5 and 100)。目前我們的射手有40%的機率會隨機從0-90度中選擇一個角度來射擊，有60%的機率會從曾經射擊過的路線中取較為精準的路線射擊。
之後短期的目標是在擁有越來越多的射擊次數之後，逐步減少隨機的概率(因為總共就只有那麼90*10^n個角度(在有限制位數的情況))在標示了大部分的射擊角度與結果之後 找出最容易射中固定靶(目前)的角度區間

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
