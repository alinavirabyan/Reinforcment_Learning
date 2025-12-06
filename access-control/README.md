**Access-control**

The project demonstrates how to use differential semi-gradient Sarsa for average-reward reinforcement learning on the Access-Control Queue problem. The agent learns when to accept or reject customers of different priorities while managing a limited number of servers. Because the task is continuous, the algorithm optimizes long-term average reward instead of discounted return. Even though the implementation is tabular, it fits naturally into the function-approximation framework. The final policy learns to prefer high-priority customers and use server capacity efficiently.

[access_control.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/access-control/src/access_control.py)

* Implements **differential semi-gradient Sarsa** for the Access-Control Queue problem with tile coding.
* Models environment with **server availability, customer priorities, and rewards**.
* `ValueFunction` class estimates **state-action values** and maintains **average reward**.
* Agent follows an **ε-greedy policy** and updates value weights during learning.
* Training loop records **state visit frequencies** and improves the policy over time.

[tile_coding.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/access-control/src/tile_coding.py)

* Provides **tile-coding utilities** from R. Sutton for function approximation in RL.
* `IHT` (Index Hash Table) manages **hash collisions** for mapping coordinates to indices.
* `hash_coords` converts coordinates into **hash indices** using either IHT or integer size.
* `tiles` maps **float and integer state variables** into a list of active tile indices.
* Enables **efficient feature representation** for continuous or discrete state spaces in RL.

[access_control.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/access-control/notebooks/access_control.ipynb)

* **Task:** Decide whether to accept or reject incoming customers on 10 servers to maximize long-term reward.
* **Environment:** Customers have 4 priority levels; queue is infinite; busy servers free probabilistically.
* **Approach:** Uses **differential semi-gradient SARSA** with tile coding for value estimation.
* **Learning:** Tabular state-action values for each `(free servers × priority)` pair; ε-greedy policy is applied.
* **Results:** Produces learned **policy and state-value plots**, showing when to accept high-priority customers based on server availability.

