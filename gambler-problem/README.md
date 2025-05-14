# **GAMBLER PROBLEM IMPLEMENTATION**

The gambler's problem is a classic example in reinforcement learning, where an agent (the gambler) must make decisions to maximize their chance of reaching a goal. It involves balancing risk and reward, as the agent has to decide how much money to bet on each flip. The goal is to find the optimal strategy (policy) for betting that maximizes the likelihood of reaching the target amount, while minimizing the risk of losing everything. This project implements the Gambler’s Problem using Value Iteration.

The project consists of the following file:

[gamblers_problem.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gambler-problem/notebooks/gamblers_problem.ipynb)
- The code models the gambler's problem, where the goal is for the gambler to reach 100 dollars by betting on coin flips, with each state representing the gambler's capital.

- The policy is determined by using value iteration, where at each step, the best stake (action) is chosen to maximize the probability of reaching the goal.

- The state-value function is updated iteratively, considering the probability of winning or losing a bet on each flip based on the current capital and the stake.

- The process continues until the value function converges, i.e., the change between successive sweeps becomes smaller than a predefined threshold.

- The final plot shows how the value function evolves over iterations and the optimal policy (stake) for each capital level.
