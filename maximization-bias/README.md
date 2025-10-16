# **Understanding Maximization Bias in Reinforcement Learning Algorithms**

This project explores how maximization bias affects action selection in a simple two-state environment and compares four reinforcement learning algorithms: Q-Learning, Double Q-Learning, Expected SARSA, and Double Expected SARSA. In the environment, State A offers two actions—“right” leads directly to the terminal state, while “left” moves to State B, which has ten stochastic actions with noisy rewards. Standard Q-Learning tends to overestimate the value of actions in State B due to noise, causing the agent to choose “left” less cautiously. Double Q-Learning reduces this bias by maintaining two independent Q-value tables and using one to update the other, leading to more reliable action selection in State A. Similarly, Expected SARSA computes the expected value under an ε-greedy policy, and its double variant further mitigates overestimation by alternating updates between two tables. The results show that bias-reduced methods, Double Q-Learning and Double Expected SARSA, more consistently choose the safer “left” action in State A, illustrating how addressing maximization bias improves policy quality.

[maximization_bias.py](maximization-bias/src/maximization_bias.py)

* The code models a simple environment with states A, B, and terminal to illustrate maximization bias.
* Hyperparameters include action-value tables, actions, transitions, ε (exploration), α (step size), and γ (discount).
* `choose_action` implements ε-greedy action selection, balancing exploration and exploitation.
* `take_action` gives reward 0 in state A and a noisy reward from N(−0.1,1) in state B.
* `q_learning` updates Q-values for either standard Q-Learning or Double Q-Learning and counts “left” actions in state A.
* Double Q-Learning reduces overestimation by alternating updates between two Q-tables, using one to select actions and the other to compute targets.

[maximization_bias.ipynb](maximization-bias/notebooks/maximization_bias.ipynb)
* The code sets up a small two-state MDP to demonstrate maximization bias, where state A has two actions and state B has multiple actions with noisy rewards.
* It imports the `q_learning` function and initial `state_action_values` from the `maximization_bias` module and displays images of the MDP and its learning curves.
* The code runs 1000 independent simulations, each consisting of 300 episodes, tracking how often the “left” action is chosen in state A for both Q-learning and Double Q-learning.
* Deep copies of the action-value tables are made for each algorithm to prevent updates from interfering across runs.
* During each episode, the `q_learning` function updates the Q-values and counts the number of “left” actions, storing the results in separate arrays for both algorithms.
* Finally, it calculates the mean proportion of “left” actions across runs, plots the learning curves comparing Q-learning, Double Q-learning, and the optimal policy, and saves the figure.
