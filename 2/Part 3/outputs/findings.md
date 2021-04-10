# Procedure of making A matrix

- Matrix A stores the probabilities of moving in or out of a given state.
- For every entry *A<sub>ij<sub>* for the matrix, *i* is an index corresponding to a certain state and *j* is an index corresponding to a certain **(state,action)** pair. So, to calculate *A<sub>ij<sub>*:
    - For every outgoing state *s*, let *p* by the probability of obtaining *s* when performed given action in given state and let *x* be the index of *s*.
    - Then we simply do<br>`A[i][j] += p` and<br> `A[x][j] -= p`
- This method basically stores the difference of outgoing and incoming probabilities for every **(state,action)** pair.

---

# Procedure of finding Policy

- x stores the number of times a particular action has to be taken from a state *s*.<br>Hence, in a solution of *x* where *Rx* is maximised, a higher value of any element of *x* would mean that it corresponds to a better action.
- To find the optimal policy, we need to find the best action for each possible state.
- To find the best action for a state *s*, from the positions in *x* which correspond to actions of *s* we find the action *a* such that among all the values of these positions of *x*, the value at the position corresponding to **(*s*,*a*)** is the maximum. Then this action *a* is the best action for state *s*.

# Analysis of Policy

- In **West Square**-
    - When *MM* is in dormant state, if *IJ* has sufficient arrows then he chooses to *SHOOT* in some cases. Otherwise *IJ* chooses to *STAY* or move *RIGHT* based on *MM*s health.
    - When *MM* is in ready state, *IJ* usually chooses to *STAY* in the same location when he has less arrows, and *SHOOT* when he has sufficient arrows. Very rarely he chooses to go *RIGHT*.
- In **North Square**-
    - When *MM* is in dormant state, *IJ* moves *DOWN* when he has no material and he has arrows or when he has sufficient arrows. Otherwise he mostly uses *CRAFT* when he has materials and he uses *STAY* when he doesn't have any materials.
    - When *MM* is in ready state, *IJ* mainly uses *CRAFT* when he has materials and he has less than 3 arrows. Otherwise he uses *STAY*
- In **East Square**-
    - When *MM* is in dormant state, *IJ* always attacks. Depending on how many arrows he has and *MM*s health *IJ* attacks with *SHOOT* or *HIT*.
    - When *MM* is in ready state, *IJ* always attacks with the same conditions as in dormant state. Except *IJ* chooses to attack by *HIT* irrespective of the number of arrows he has when *MM* has full health.
- In **South Square**-
    - When *MM* is in dormant state, *IJ* chooses to *UP* mainly when he has sufficient arrows, or *MM* has high health. Otherwise, if he has materials less than 2, then he uses *GATHER* depending on the number of arrows he has, and in the other case uses *STAY*.
    - When *MM* is in ready state, *IJ* usually chooses to *GATHER* when *MM* does not have full health, and chooses *STAY* in all other cases.
- In **Center Square**-
    - When *MM* is in dormant state, *IJ* attacks depending on how many materials he has. If he has no materials, depending on the number of arrows *IJ* has, and *MM*s health he chooses to *SHOOT*, *HIT* or go *RIGHT* to attack with a greater chance. If he has materials, he might choose to go *UP* to *CRAFT* some arrows.
    - When *MM* is in ready state, if *IJ* is low on materials he goes *DOWN*, if he is low on arrows and has materials he goes *UP*. Otherwise he attacks with *SHOOT* depending on *MM*s health, or goes *LEFT* away from *MM*s attack zone.

---

# Can there be multiple Policies? Why?

- Multiple Policies are **possible**.
- In the method described to find the policy, for a state *s* if the set of all positions in *x* which correspond to actions on *s* is *S*, then it is possible that the maximum of values of *x* for psotions in *S* is shared by more than one positions.
- In our code, we are taking the first position in *S* whose value in *x* is the maximum among all values of the positions in *S*.
- If we randomize the positions whose values in *x* are the maximum, or choose any of them except the first, we can obtain a different policy.
- Changing the matrix A can also change the policy. Matrix A stores the probabilities of moving in or out of a given state, and changing them would change state utilities, reward matrix R, and hence variable matrix *x*.
- Our policy can change if we change the starting state \\alpha. This is because changing \\alpha changes our constraints on variable matrix *x*.
- Changing reward matrix R would change the condition of maximizing *Rx*, and hence it can easily affect the policy.

---