Dynamic programming (DP) methods solve finite Markov Decision Processes (MDPs) using **policy iteration** and **value iteration**.

* **Policy evaluation** computes the value function for a given policy, while **policy improvement** updates the policy based on the value function.
* DP methods update state values using the Bellman equation until convergence, providing optimal policies and value functions.
* **Generalized Policy Iteration (GPI)** combines policy evaluation and improvement to iteratively improve both the policy and value function, often leading to optimal solutions.
* **Asynchronous DP methods** update states in arbitrary orders for more efficient computations.
* **Bootstrapping** updates estimates of state values based on other estimates, a technique also used in reinforcement learning methods.

Project consist of the following main files:

[grid_world.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gridworld-dp/notebooks/grid_world.ipynb)



* **Gridworld Setup**:

  * The grid is 4x4 with non-terminal states and 1 terminal state.
  * There are 4 possible actions per state (up, down, left, right), which move the agent in the corresponding direction, unless the agent would move off the grid, in which case it stays in the same state.
  * The task is episodic and undiscounted.
  * The reward is -1 for all transitions until the agent reaches the terminal state.

* **Policy and Evaluation**:

  * The agent follows a random policy (equiprobable random choice of actions).
  * The **value function** is computed iteratively via policy evaluation, showing the expected reward for all states under the current policy.
  * The final value function represents the negation of the expected number of steps from each state to the terminal state.

* **Policy Iteration and Improvement**:

  * **Policy Iteration**:

    * The left column of the figure shows the sequence of value functions for the random policy.
    * The right column shows the greedy policies derived from the value functions.
    * The last policy is an improvement over the random policy, and after a few iterations, the policy is optimal.
    * The final greedy policy makes moves that minimize the number of steps to reach the terminal state.
  * **Policy Improvement**:

    * Policy improvement happens when a random policy is updated to a greedy policy based on the value function.
    * Even though a policy improvement is guaranteed, the new policy may not always be optimal.
    * In this case, after policy improvement, the new policy is optimal.
   
* **Convergence**:

  * Policy iteration converges quickly in this example and finds the optimal policy in just one iteration.
  * The policy improvement theorem guarantees that the new policies are better than the random policy.
  * After a few iterations, policy iteration finds the optimal policy that leads to the terminal state in the fewest steps.

   [grid_world.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gridworld-dp/src/grid_world.py) - This Python code simulates a 4x4 gridworld where an agent moves through different states based on actions like left, up, right, and down. The agent receives a reward of -1 for every move, except when it reaches terminal states at the top-left and bottom-right corners, which provide a reward of 0. The code calculates the state-value function, which represents the expected future rewards from each state, using an iterative policy evaluation method. The agent follows a random policy initially, and the state values are updated until they converge to stable estimates. The program helps in understanding the process of value iteration for a gridworld environment in reinforcement learning.


