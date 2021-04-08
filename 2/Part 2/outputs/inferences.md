# Inferences

---

## Task 1

> Gamma = 0.999
> Delta = 0.001
> Iteration required to converge: 118

From the trace file `part_2_trace.txt`, we can infer the following about the final policy:
- In **West Square**-
    - When *MM* is in dormant state, if *IJ* has sufficient arrows then he chooses to *SHOOT* when *MM* has low health, and otherwise he moves *RIGHT* to attack *MM* with *HIT* before *MM* comes back to ready state.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range if he has arrows and *MM*s health is low, otherwise he moves *RIGHT* to *HIT*, *CRAFT* or *GATHER*, depending on how much material he has and *MM*s health. Depending on his arrows and *MM*s health, *IJ* chooses to *SHOOT* or *STAY*.
- In **North Square**-
    - When *MM* is in dormant state, *IJ* moves *DOWN* when he has no material, he has sufficient arrows or *MM*s health is 25 and *IJ* has 1 arrow. In all other cases *IJ* chooses to *CRAFT* arrows.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range. *IJ* chooses to *STAY* when he has no material or when he has 3 arrows. Otherwise *IJ* chooses to *CRAFT*. *IJ* chooses to go *DOWN* to *GATHER* material when he *MM*s health is full, and he doesn't have sufficient arrows and no material. Also *IJ* chooses to *STAY* when he has sufficient arrows and *MM*s health is 25.
- In **East Square**-
    - When *MM* is in dormant state, *IJ* always attacks. When he is out of arrows, or when *MM* has full health and *IJ* does not have all his arrows he attacks with *HIT*. Otherwise he attacks by *SHOOT*.
    - When *MM* is in ready state, *IJ* still attacks. When he is out of arrows, or when *MM* has full health he attacks with *HIT*. Otherwise he attacks by *SHOOT*.
- In **South Square**-
    - When *MM* is in dormant state, *IJ* chooses to *GATHER* only when he does not have arrows and materials, and when *MM*s health is 25. In all other case he goes *UP* to attack or *CRAFT*.
    - When *MM* is in ready state, *IJ* goes *UP* when *MM*s health is 100 and he has insufficient arrows, or when he has 2 materials and insufficient arrows. He either chooses to *GATHER* materials or *STAY* depending on how many materials and arrows he has.
- In **Center Square**-
    - When *MM* is in dormant state, *IJ* moves *RIGHT* to attack when he has no materials, and moves *UP* to craft or again *RIGHT* to attack depending on how many arrows he has and *MM*s health.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range by going *UP* or *DOWN*. When *IJ* has sufficient arrows, he goes *LEFT* to attack *MM* by shooting. If *IJ* jas arrows and *MM*s health is 25, he attacks *MM* by *SHOOT*.

---

## Task 2

### Case 1

> Gamma = 0.999
> Delta = 0.001
> Iteration required to converge: 119

From the trace file `part_2.1_trace.txt`, we can infer the following about the final policy:
- In **West Square**-
    - When *MM* is in dormant state, if *IJ* has sufficient arrows then he chooses to *SHOOT* when *MM* has low health, and otherwise he moves *RIGHT* to attack *MM* with *HIT* before *MM* comes back to ready state.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range if he has arrows and *MM*s health is low, otherwise he moves *RIGHT* to *HIT*, *CRAFT* or *GATHER*, depending on how much material he has and *MM*s health. Depending on his arrows and *MM*s health, *IJ* chooses to *SHOOT* or *STAY*.
- In **North Square**-
    - When *MM* is in dormant state, *IJ* moves *DOWN* when he has no material, he has sufficient arrows or *MM*s health is 25 and *IJ* has 1 arrow. In all other cases *IJ* chooses to *CRAFT* arrows.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range. *IJ* chooses to *STAY* when he has no material or when he has 3 arrows. Otherwise *IJ* chooses to *CRAFT*. *IJ* chooses to go *DOWN* to *GATHER* material when he *MM*s health is full, and he doesn't have sufficient arrows and no material. Also *IJ* chooses to *STAY* when he has sufficient arrows and *MM*s health is 25.
- In **East Square**-
    - When *MM* is in dormant state, *IJ* always attacks. When he is out of arrows, or when *MM* has full health and *IJ* does not have all his arrows he attacks with *HIT*. Otherwise he attacks by *SHOOT*.
    - When *MM* is in ready state, *IJ* still attacks. When he is out of arrows, or when *MM* has full health he attacks with *HIT*. Otherwise he attacks by *SHOOT*.
- In **South Square**-
    - When *MM* is in dormant state, *IJ* chooses to *GATHER* only when he does not have arrows and materials, and when *MM*s health is 25. In all other case he goes *UP* to attack or *CRAFT*.
    - When *MM* is in ready state, *IJ* goes *UP* when *MM*s health is 100 and he has insufficient arrows, or when he has 2 materials and insufficient arrows. He either chooses to *GATHER* materials or *STAY* depending on how many materials and arrows he has.
- In **Center Square**-
    - When *MM* is in dormant state, *IJ* moves *RIGHT* to attack when he has no materials, and moves *UP* to craft or again *RIGHT* to attack depending on how many arrows he has and *MM*s health.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range by going *UP* or *DOWN*. When *IJ* has sufficient arrows, he goes *LEFT* to attack *MM* by shooting. If *IJ* jas arrows and *MM*s health is 25, he attacks *MM* by *SHOOT*.

### Case 2

> Gamma = 0.999
> Delta = 0.001
> Iteration required to converge: 57

From the trace file `part_2.2_trace.txt`, we can infer the following about the final policy:
- In **West Square**-
    - When *MM* is in dormant state, if *IJ* has sufficient arrows then he chooses to *SHOOT* when *MM* has low health, and otherwise he chooses to *STAY*.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range. Depending on his arrows and *MM*s health, *IJ* chooses to *SHOOT* or *STAY*.
- In **North Square**-
    - When *MM* is in dormant state, *IJ* moves *DOWN* when he has no material, He chooses to *STAY* when he has sufficient arrows and *MM*s health is not too much. In all other cases *IJ* chooses to *CRAFT* arrows.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range. *IJ* chooses to *STAY* when he has no material or when *MM* has high health. Otherwise *IJ* chooses to *CRAFT*.
- In **East Square**-
    - When *MM* is in dormant state, *IJ* attacks when *MM*s health is low. When he is out of arrows he attacks with *HIT*. Otherwise he attacks by *SHOOT*. When *MM* has high health *IJ* moves *LEFT*.
    - When *MM* is in ready state, *IJ* attacks with *SHOOT* when *MM*s health is very low and he has sufficient arrows. Otherwise he goes *LEFT*.
- In **South Square**-
    - When *MM* is in dormant state, *IJ* chooses to *STAY* when he sufficient arrows. In all other case he goes *UP* to attack or *CRAFT*.
    - When *MM* is in ready state, *IJ* always chooses to *STAY*.
- In **Center Square**-
    - When *MM* is in dormant state, when *MM* health is high *IJ* moves *LEFT*. Otherwise if he has sufficient arrows then he attacks with *SHOOT*, if he has materials he moves *UP*, otherwise he moves *RIGHT*.
    - When *MM* is in ready state, when *MM* health is high *IJ* moves *LEFT*. Otherwise if he has sufficient arrows then he moves *UP*.

### Case 3

> Gamma = 0.25
> Delta = 0.001
> Iteration required to converge: 8

From the trace file `part_2.3_trace.txt`, we can infer the following about the final policy:
- In **West Square**-
    - When *MM* is in dormant state, if *IJ* has arrows then he chooses to *SHOOT*. Otherwise he chooses to *STAY* when *MM*s health is high and move *RIGHT* when health is low.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range. If *IJ* has arrows, he chooses to *SHOOT*, otherwise he chooses to *STAY*.
- In **North Square**-
    - When *MM* is in dormant state, *IJ* moves *DOWN* when *MM*s health is low. Otherwise, he chooses to *STAY* when he has no material and *CRAFT* when he has materials.
    - When *MM* is in ready state, *IJ* tries to stay out of *MM*s attack range. *IJ* goes *DOWN* when he has arrows. Otherwise he chooses to *CRAFT* when he has materials, and *STAY* when he doesn't.
- In **East Square**-
    - When *MM* is in dormant state, *IJ* attacks with *SHOOT* when *MM*s health is low and he has arrows, otherwise he attacks by *HIT*.
    - When *MM* is in ready state, *IJ* attacks with *SHOOT* when *MM*s health is very low and he has arrows, he attacks with *HIT* when *MM*s health is not very high, otherwise he goes *LEFT*.
- In **South Square**-
    - When *MM* is in dormant state, *IJ* chooses to *GATHER* when *MM*s health is high and to go *UP* when health is low.
    - When *MM* is in ready state, *IJ* goes up when *MM*s is the least and he has arrows. Otherwise he chooses to *GATHER*.
- In **Center Square**-
    - When *MM* is in dormant state, when *MM* health is high *IJ* moves *LEFT*. Otherwise if he has arrows and *MM*s health is least he attacks with *SHOOT*, and otherwise he attacks with *HIT*.
    - When *MM* is in ready state, when *MM* health is high *IJ* moves *LEFT*. Otherwise if he has arrows and *MM*s health is least he attacks with *SHOOT*, and otherwise he attacks with *HIT*.
