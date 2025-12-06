**Mountain-car-et**

[mountain_car.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/mountain-car-et/src/mountain_car.py)

1. This code implements SARSA(λ) with tile coding for the Mountain Car problem, including multiple eligibility trace types: accumulating, Dutch, replacing, and replacing with clearing.
2. It defines the environment dynamics in the `step` function and an ε-greedy action selection in `get_action`, though exploration is set to zero here.
3. The `SARSA` class handles feature extraction with tile coding, computes value estimates, updates eligibility traces, and adjusts weights using the TD error.
4. Different trace update rules are applied depending on the chosen eligibility trace method, including clearing non-selected action tiles when needed.
5. The `play` function runs one episode using the current SARSA evaluator, updating weights at each step and returning the total number of steps to reach the goal or hitting the step limit.

[tile_coding.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/mountain-car-et/src/tile_coding.py)

1. This code implements tile coding utilities from Sutton’s reinforcement learning framework, including an Index Hash Table (IHT) and coordinate hashing.
2. The `IHT` class manages a fixed-size dictionary for mapping objects (like state-action tuples) to unique indices, handling collisions if the table becomes full.
3. The `hash_coords` function converts a set of coordinates into a single index, using the IHT if provided, or falling back to a simple hash modulo operation.
4. The `tiles` function maps continuous and integer state variables to a set of tile indices, creating multiple overlapping tilings for generalization.
5. These utilities are essential for implementing function approximation with tile coding in reinforcement learning, allowing efficient representation of large or continuous state spaces.

[mountain_car.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/mountain-car-et/notebooks/mountain_car.ipynb)
1. The code evaluates **SARSA(λ)** on the Mountain Car task, testing how the trace-decay parameter λ, step size α, and trace type affect learning.
2. In the first experiment, λ and α are varied using replacing traces, measuring steps to reach the goal over 50 episodes and 30 runs.
3. In the second experiment, different eligibility trace types are compared at λ=0.9, recording rewards for 20 episodes and 30 runs.
4. Results show that higher λ generally improves early learning and some traces are more stable than others at high step sizes.
5. The plots (Figures 12.10 and 12.11) summarize the performance, illustrating the impact of trace decay, step size, and trace type on SARSA learning.

