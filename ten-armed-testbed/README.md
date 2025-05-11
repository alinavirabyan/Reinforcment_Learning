

###  10-ARMED-TESTBED IMPLEMENTATION

This project demonstrates various strategies for solving the **multi-armed bandit problem**, which involves finding the right balance between **exploration** (trying new actions to gain information) and **exploitation** (choosing actions known to give high rewards).

Several popular methods are implemented and compared:

* **ε-greedy**: Selects the best-known option most of the time but occasionally chooses a random action to encourage exploration.
* **UCB (Upper Confidence Bound)**: Selects actions based on both their reward and how often they have been chosen, promoting exploration of less-tested actions.
* **Gradient Bandits**: Uses preferences for actions and chooses them probabilistically using a softmax function, favoring more preferred actions.
* **Optimistic Initialization**: Starts with high initial value estimates for all actions, encouraging early exploration even in greedy algorithms.

These methods are tested using a standard 10-armed bandit setup. Since each method includes a key parameter (like ε in ε-greedy), performance is evaluated across a range of values. To simplify comparison, the **average reward over 1000 steps** is used instead of displaying individual learning curves.

Key findings include:

* Each method performs best at an intermediate parameter value—neither too low nor too high.
* Most methods are robust across a wide range of parameter settings.
* **UCB achieved the best overall performance** in these experiments.

Advanced approaches such as the **Gittins index** and **Thompson sampling** (Bayesian methods) are also discussed. Although theoretically optimal in some cases, they often require complete prior knowledge or are computationally too complex for general use. These ideas transition into full **reinforcement learning**, which is covered in later stages of this project.

The project consists of the following main files:

[ten-armed-testbed.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/ten-armed-testbed/src/ten-armed-testbed.ipynb) 

The code simulates different strategies for solving the multi-armed bandit problem, where an agent selects actions to maximize rewards over time. It compares various action selection methods, including **greedy** and **ε-greedy** approaches, by running multiple simulations and tracking the **average reward** and **percentage of optimal actions** selected.

Key experiments include:

1. **Reward distribution**: Visualizes how rewards are distributed for different actions.
2. **Greedy vs. ε-greedy**: Compares exploration vs. exploitation strategies with varying levels of exploration (ε values).
3. **Optimistic vs. Realistic Initialization**: Tests how initial action values affect exploration behavior.
4. **Upper Confidence Bound (UCB) and Gradient Bandit Algorithms (GBA)**: These strategies would be tested to see how they perform in maximizing rewards and selecting optimal actions (though the code for these is not fully implemented here).

The results help to understand how different strategies balance exploration and exploitation to maximize rewards over time.



 
[bandit.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/ten-armed-testbed/src/bandit.py) 

This file defines the core `Bandit` class used to simulate the 10-armed bandit environment.
It supports several action-selection strategies, including:

* **ε-greedy**
* **Upper Confidence Bound (UCB)**
* **Optimistic Initialization**
* **Gradient Bandit Algorithm (GBA)**

Key features:
* Allows choosing between sample-average updates and constant step-size updates.
* Supports tracking optimal actions, rewards, and time steps.
* Implements softmax preferences and optional baselines for gradient methods.

The `Bandit` class provides three main functions:

* `__init__()`: Sets up the bandit with various strategy parameters.
* `initialize()`: Resets the bandit environment with new random action values.
* `act()`: Selects an action based on the configured strategy.
* `step(action)`: Simulates taking an action, returns a reward, and updates internal estimates.
?


