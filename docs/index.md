---
layout:  default 
title:  Status
---

###Once upon a time...
      There was a little boy called Q. He lived in a wonderland named DBH. People in DBH live happily together. They sing, they dance, and they code together! Suddenly, a group of mob broke into the village, they rob and bully the residents in DBH. From then on, mob came to the village occasionally. Q cannot stand mobs bullying their family and friends. He decides to learn archery to defense the mobs and protect the residents in DBH. However, Q doesn’t have that much arrows. Our job is to help Q to improve his archery skill so that he can kill the mob using fewest arrows. We used Q-learning from Reinforcement learning to achieve this goal. And we received a pretty good result
<img src="images/e44.png">


Source code: https://github.com/shaoyih/One-Shot

Reports:

- [Proposal](proposal.md)
- [Status](status.md)
- [Final](final.md)

## Goal

First goal of our project is to let the agent to shoot a motionless target:

As the graph shown above, the target is standing right in front of us. Agent can only change it's up/down angle to aim at the mob.

Second goal of our project is to let the agent to shoot a moving-horizontally target:

More goals are coming!

## Environment setting
We're have two rectangle stages separated by a 2 block-length air gap, where Mob is standing on one stage, agent is facing the mob on the other. We chose Zombie as the Mob(target). Zombie has a 15 life long(3 shot). Time is set to sunset so that Zombie can still live. Peacons and Glowstone are used as our light resource.


## trailor

<iframe width="560" height="315" src="https://www.youtube.com/embed/Fw2nhFTxk3Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


[quickref]: https://github.com/mundimark/quickrefs/blob/master/HTML.md
