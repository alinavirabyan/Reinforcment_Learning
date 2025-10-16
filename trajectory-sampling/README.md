# **Trajectory Sampling – Expected vs On-Policy Updates**

This project investigates how the distribution of updates influences learning speed and policy quality in planning-based reinforcement learning. It compares **uniform sampling**, which updates all state–action pairs evenly, with **on-policy sampling**, which focuses updates on states visited by an ε-greedy policy. Experiments show that on-policy sampling accelerates early learning by concentrating on relevant trajectories. However, uniform sampling eventually achieves higher long-term accuracy due to broader coverage of the environment. The study highlights the trade-off between **focus** and **coverage** in expected updates. Overall, it demonstrates that balancing these approaches is key to efficient and stable convergence in planning.

[trajectory_sampling.ipynb](trajectory_sampling.ipynb)


* Uses **one-step expected updates** to isolate the effect of the **update distribution** on learning.
* Compares **uniform sampling** (updates every state–action pair cyclically) with **on-policy sampling** (updates only visited pairs under an ε-greedy policy).
* Experiments are performed on **randomly generated episodic tasks**, with configurable numbers of states, branching factors, and transition probabilities.
* **Evaluates the greedy policy** by computing the value of the start state at any point in the planning process.
* Plots policy quality (value of the start state) vs. computation time for different **state sizes** (1,000 and 10,000) and **branching factors** (1, 3, 10).
* Demonstrates that **on-policy updates accelerate early learning**, especially for smaller branching factors, while **uniform updates eventually achieve higher long-term accuracy**.

[trajectory_sampling.py](trajectory_sampling.py)

* **Defines the MDP Task environment** (`Task` class) with random transitions, Gaussian rewards, and terminal probabilities.
* Implements **helper functions**, including `argmax()` for ε-greedy action selection with random tie-breaking and `evaluate_policy()` for Monte Carlo evaluation of the greedy policy.
* Provides **uniform sampling** updates, which cycle through all state–action pairs and compute expected value updates for even coverage of the environment.
* Provides **on-policy sampling** updates, which follow trajectories under an ε-greedy policy and focus computation on visited states for faster early learning.
* Uses **parallel processing** (`ProcessPoolExecutor`) to run multiple tasks in parallel and average results efficiently (`run_experiment()`).
* Collects and returns **performance data** (steps vs. average return) for each method, enabling comparison of learning speed and policy quality.

