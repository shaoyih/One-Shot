---
layout:  
title:  one-Shot
---

Source code: https://github.com/shaoyih/One-Shot

Reports:

- [Proposal](proposal.md)
- [Status](status.md)
- [Final](final.md)

<h3>Goal</h3>
First goal of our project is to let the agent to shoot a motionless target:

As the graph shown above, the target is standing right in front of us. Agent can only change it's up/down angle to aim at the mob.

Second goal of our project is to let the agent to shoot a moving-horizontally target:

More goals are coming!

<h3>Environment setting</h3>
We're have two 10 * 10 stages separated by a 3 block-length gap, where Mob is standing on one stage, agent is facing the mob on the other. We chose Zombie as the Mob(target). Zombie has a 15 life long(3 shot). Time is set to sunset so that Zombie can still live. Peacons and Glowstone are used as our light resource.



Just getting started with Markdown?
See the [HTML <-> Markdown Quick Reference (Cheat Sheet)][quickref].


[quickref]: https://github.com/mundimark/quickrefs/blob/master/HTML.md
