**Mountain-car**

[tile_coding.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/mountain-car/src/tile_coding.py)

1. This code provides utilities for **tile coding**, a method to discretize continuous variables for reinforcement learning.
2. The `IHT` class (Index Hash Table) manages indices for tiles, handling collisions when more unique tiles exist than the table size.
3. The `get_index` method either returns an existing index for an object or assigns a new one, using hashing if the table is full.
4. The `hash_coords` function converts a set of coordinates into a single integer index, using either an `IHT` object or a simple modulo hash.
5. The `tiles` function maps continuous and integer variables to multiple tile indices, generating offsets for each tiling to improve generalization.

[mountain_car.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/mountain-car/src/mountain_car.py)


1. This code implements **semi-gradient n-step SARSA** for the Mountain Car problem using tile coding to approximate the state-action value function.
2. The `ValueFunction` class represents the state-action value function and uses tile coding to map continuous position and velocity into discrete features with associated weights.
3. The `get_action` function selects an action using an ε-greedy policy based on the estimated values, defaulting to fully greedy since exploration probability is 0.
4. The `step` function simulates the environment dynamics, updating position and velocity based on the chosen action and returning a reward of -1 at each time step.
5. The `semi_gradient_n_step_sarsa` function runs episodes, updates the value function using n-step returns, and `print_cost` visualizes the learned cost-to-go function over a grid of positions and velocities.

[mountain_car.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/mountain-car/notebooks/mountain_car.ipynb)

* Mountain Car: underpowered car must build momentum by first moving away from the goal.
* States: continuous position and velocity; actions: forward, reverse, zero.
* Tile coding converts continuous states to binary features for linear value approximation.
* Semi-gradient n-step SARSA updates the value function; optimistic initialization drives exploration.
* Multi-step updates (n > 1) accelerate learning and improve final performance.
* Step size and n-step parameters strongly affect learning speed and stability.
