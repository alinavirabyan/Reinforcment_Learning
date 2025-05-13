**RANDOM WALK IMPLEMENTATION**

The Random Walk is a Markov Reward Process (MRP) with a fixed set of states and no actions, used to study prediction tasks in reinforcement learning. It begins from a central state and transitions left or right with equal probability until reaching terminal states at either end. The agent receives +1 reward only when it reaches the right terminal state; otherwise, the reward is 0. Since it's an undiscounted problem, the value of each state is simply the probability of eventually reaching the right terminal state from that state.


The project consists of the following files:

[random_walk.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/random-walk/notebooks/random_walk.ipynb):

1.Value Initialization & Plotting: The code initializes value estimates for the non-terminal states and compares them against the true values using plots after 0, 1, 10, and 100 episodes of Temporal-Difference (TD(0)) learning.

2.TD vs MC Performance Measurement: It runs 100 simulations using both TD(0) and Monte Carlo (MC) methods for various learning rates (α), tracking the root mean square error (RMSE) between learned and true values.

3.Dynamic Learning: In each episode, the value function is updated using either TD(0) or MC, and RMSE is recorded at each step to measure learning progress.

4.Batch Updating: A batch version of the algorithm is also tested, where all previously seen episodes are reused multiple times until convergence for both TD and MC methods.

5.Final Evaluation: For both incremental and batch training, RMSE curves are plotted to compare how well each method learns over time.

6.Key Insight: Despite MC being optimal for minimizing sample return error, TD outperforms MC in terms of predicting expected returns, making it a more effective method in this context.

[random_walk.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/random-walk/src/random_walk.py):

Sure, here's a clean, bulleted explanation without stickers:

1.The code defines a random walk problem with 7 states: two terminal states (0 and 6) and five non-terminal states (1 to 5), with the agent always starting at state 3.

2.It initializes the true values based on the probability of reaching the right terminal state and sets approximate initial values for learning.

3.Two learning methods are implemented: Monte Carlo (MC), which updates values after each episode, and Temporal Difference (TD), which updates values at each step.

4.The `batch_updating` function collects trajectories and rewards from multiple episodes and uses batch updates to improve value estimates until convergence.

5.The code performs 100 runs for better accuracy and stability of results by averaging the outcomes.

6.It computes and returns the RMSE (Root Mean Square Error) between the learned and true state values to evaluate the performance of the algorithms.
