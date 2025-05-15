# **CLIFF-WALKING IMPLEMENTATION**
Cliff Walking is a common example used to compare on-policy methods like Sarsa and off-policy methods like Q-learning in reinforcement learning. Q-learning often finds the optimal path but may fall off the cliff due to exploration, while Sarsa learns a safer, though longer, route. Expected Sarsa improves on Sarsa by calculating the expected value of future actions, which reduces variance and generally performs better. Temporal-Difference learning combines ideas from Monte Carlo and dynamic programming to address both prediction and control problems. These TD methods are popular because they are simple, efficient, and can learn directly from experience with minimal computation.

The project consists of the following files:

[cliff_walking.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/cliff-walking/notebooks/cliff_walking.ipynb)

1. **The Cliff Walking environment** is used to compare SARSA (on-policy) and Q-learning (off-policy) by simulating an agent navigating a grid from start to goal, where falling into the cliff gives a penalty of -100.
2. **SARSA** updates its action-value function based on the actual action taken, leading it to learn a **safer path** away from the cliff, while **Q-learning** learns the **optimal path** near the cliff but risks falling due to exploration (ε-greedy strategy).
3. The code runs **multiple episodes across several independent runs**, collecting and averaging rewards to compare learning performance between the two methods.
4. It initializes **reward arrays** and **action-value matrices** for both SARSA and Q-learning, and iteratively updates them using their respective algorithms.
5. The first part of the code visualizes the **learning curve** of both algorithms, showing that SARSA performs better during training despite Q-learning eventually finding the optimal path.
6. The second part compares **asymptotic vs. interim performance** of SARSA, Expected SARSA, and Q-learning under different step sizes (α values).
7. The results are plotted to show how each method performs over time and under different learning rates, helping us understand **learning stability and efficiency** of each algorithm.


[cliff_walking.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/cliff-walking/src/cliff_walking.py)

1. This code solves the **Cliff Walking** problem using reinforcement learning algorithms: SARSA, Expected SARSA, and Q-Learning.
2. The environment is a 4x12 grid where the agent starts at one point and must reach the goal without falling off the cliff.
3. The `step` function moves the agent based on its action and returns the next state and reward, applying a penalty for falling off the cliff.
4. The `choose_action` function implements an ε-greedy strategy to balance exploration (random actions) and exploitation (choosing the best-known action).
5. The `sarsa` and `q_learning` functions simulate one full episode and update the action-value table (`Q`) using their respective learning rules.
6. The `print_optimal_policy` function prints the best path the agent has learned, using arrows (↑ ↓ ← →) to represent directions and `G` for the goal.











