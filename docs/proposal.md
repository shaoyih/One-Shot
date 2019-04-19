---
layout: default
title: Proposal
---

## Summary of Project
It's a game of archery. Our goal is to shoot the opponents until they die.Opponent also can attack back using their archery and their special shooting algorithm.Our input would be opponent_shot(yes, no), location(a tuple that locates the location of the opponent).Our output will be direction control(up, down, left, right, jump, rotate left, rotate right), shoot(yes, no),shooting degree(e.g 30 degree above air) depends on distance, shooting strength(how).


## AI/ML Algorithm
Reinforcement learning, nerual network.Probably change later.


## Evaluation
The base line our AI is to kill the skeleton opponent. Metrics include time used, shooting times and the blood for our AI and opponent. There are two stages to improve our shooting metrics. First stage is set some static targets on different distance to train our AI shooting accuracy. The second stage is to shoot moving targets and predict their block.

In a shorter time to kill the target at the same time how many live our AI still has. Our moon shoot case is opponent die in 1 min and we don't have any blood lost.


## Apointment with instructor
