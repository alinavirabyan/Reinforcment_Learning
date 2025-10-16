# RANDOM-WALK-NTD IMPLEMENTATION
This project studies n-step Temporal Difference (TD) learning using a 19-state Random Walk environment. An agent starts in the center and moves left or right with equal probability until reaching one of two terminal states, receiving a reward of −1 or +1. The goal is to estimate the value function for each non-terminal state and examine how the parameter n influences learning performance. The code implements n-step TD updates, where smaller n values increase bias but reduce variance, while larger n values decrease bias but increase variance. Multiple runs and episodes are simulated, and the results are compared to true state-values using root mean-squared error (RMSE). Visualizations show learning curves, accuracy over episodes, and the bias–variance trade-off for different n-step configurations.


[random_walk.py](./random-walk-ntd/src/random_walk.py)

* This code implements n-step Temporal Difference (TD) learning for a 19-state Random Walk environment.
* Non-terminal states are updated, and terminal states give rewards of −1 (left) or +1 (right).
* True state-values are computed using the Bellman equation as a reference for evaluation.
* The `temporal_difference` function updates state-value estimates based on n-step returns.
* Each episode starts from the middle state and records the trajectory of states and rewards.
* The code analyzes how step sizes and different n-step configurations affect learning performance and convergence.



[random_walk.ipynb](./random-walk-ntd/notebooks/random_walk.ipynb)
* This notebook demonstrates n-step Temporal Difference (TD) learning in a 19-state Random Walk environment.
* The agent starts from the center state and moves left or right with equal probability until reaching a terminal state.
* Rewards are −1 for reaching the left terminal and +1 for reaching the right terminal, with all other transitions giving 0 reward.
* The notebook computes state-value estimates for non-terminal states using n-step TD updates.
* Multiple runs and episodes are used to evaluate the effect of different step sizes and n-step parameters on learning performance.
* Root mean-squared error (RMSE) is calculated against the true state-values to visualize convergence and the bias–variance trade-off.



