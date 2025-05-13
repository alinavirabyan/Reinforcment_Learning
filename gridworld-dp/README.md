**GRIDWORLD IMPLEMENTATION WITH DYNAMIC PROGRAMMING**

This project implements the foundational concepts and algorithms of dynamic programming (DP) to solve finite Markov Decision Processes (MDPs). Policy evaluation iteratively calculates the value function for a given policy, while policy improvement derives a better policy based on the current value function. By combining these two processes, the project uses policy iteration and value iteration, which are widely used DP methods for computing optimal policies and value functions. Classical DP methods update state values in sweeps, with each update reflecting the expected value of a state based on the probabilities of its possible successor states. These updates are aligned with Bellman equations, which define the optimality conditions for value functions. Generalized Policy Iteration (GPI) provides the framework for these methods, where policy evaluation and improvement interact until they converge to an optimal policy and value function. The project also explores asynchronous DP methods, where updates occur in a non-sequential order, using out-of-date information and employing bootstrapping to refine estimates based on other estimates.

The project consists of the following main files:

[grid_world.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gridworld-dp/notebooks/grid_world.ipynb)
- The grid_world.ipynb notebook demonstrates value iteration and policy improvement in a 4x4 grid world environment.
- The agent follows a random policy and computes the state value function using dynamic programming.
- The notebook compares in-place and out-of-place computations for the state values, showing the number of iterations needed for convergence.

- It visualizes the state-value grid after each iteration to illustrate how the value function evolves.

- The policy improvement section shows how a random policy is improved based on the computed value function.

- Lastly, policy iteration is performed, and the optimal policy is derived in just one iteration, showcasing the efficiency of the method.

[grid_world.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gridworld-dp/src/grid_world.py)

- The code defines a 4x4 grid world where an agent can take four actions: left, up, right, and down, with equal probability for each action.

- The is_terminal function checks if the agent has reached the terminal state, located at either the top-left or bottom-right corners.

- The step function computes the next state and reward based on the agent's current state and action, with boundary checks to prevent going off the grid.

- The compute_state_value function calculates the state-value function using the Bellman equation, updating state values iteratively until convergence.

- The draw function visualizes the state-value function as a grid, displaying the computed values for each state in the grid world.
