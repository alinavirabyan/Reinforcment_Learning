# **INFINITE-VARIANCE IMPLEMENTATION**

The problem involves using importance sampling to estimate the value of a policy in a reinforcement learning (RL) setting. The target policy selects a specific action (left) with a goal of terminating, while the behavior policy selects actions probabilistically (right and left with equal probability). Ordinary importance sampling (OS) struggles with infinite variance and poor convergence in such scenarios, especially when the target policy is off-policy. This code demonstrates the estimation of the policy value using ordinary importance sampling over a large number of episodes and runs.

The project consists of the following main files:

[infinite_variance.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/infinite-variance/notebooks/infinite_variance.ipynb):
1. The code simulates estimating the value of a policy using **ordinary importance sampling** in an off-policy learning setting.
2. The `play()` function simulates episodes by returning a reward and an action trajectory.
3. It calculates an **importance sampling ratio** based on the last action taken, adjusting for whether the action is consistent with the target policy.
4. If the last action is "right," the ratio is 0 (because it doesn't match the target policy); otherwise, it calculates the ratio as the inverse of 0.5 raised to the action trajectory length.
5. For each episode, the weighted reward is calculated by multiplying the reward by the importance sampling ratio and stored in a list.
6. The **cumulative sum** of the weighted rewards is computed, and the ordinary importance sampling estimate is the average of these rewards up to that point.
7. The code generates a plot of the ordinary importance sampling estimates against episodes, showing the convergence (or lack thereof) to the correct policy value.

[infinite_variance.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/infinite-variance/src/infinite_variance.py):
1. **Actions Dictionary**: The `actions` dictionary maps two actions, "left" and "right," to numeric values 0 and 1, respectively.
2. **Target Policy**: The `target_policy()` function always returns "left" (action 0), representing a policy that always selects the left action with certainty.
3. **Behavior Policy**: The `behavior_policy()` function randomly selects between "left" and "right" with equal probability (50% for each), modeled using a binomial distribution.
4. **Play Function**: The `play()` function simulates an episode by continuously selecting actions based on the behavior policy and records the trajectory of actions.
5. **Action Outcomes**: If the selected action is "right," the function returns a reward of 0 and the trajectory. If the selected action is "left," there's a 90% chance it leads to termination with a reward of 1.
6. **Return Values**: The function `play()` returns the reward and the sequence of actions taken during the episode.

