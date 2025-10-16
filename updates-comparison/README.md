# **Updates Comparison – Expected vs Sample Updates**

This project examines the balance between expected and sample updates in reinforcement learning. It focuses on how computational effort influences learning accuracy and efficiency, especially when dealing with large branching factors. The experiments simulate different environments to compare how quickly each update method converges to the true value. Results show that expected updates are more accurate but computationally expensive, while sample updates are faster and more scalable. The project demonstrates that in large environments, sample-based learning achieves similar accuracy with less computation. This insight explains why modern RL algorithms like Q-learning and SARSA rely on sample updates in practice.

[expectation_vs_sample.py](expectation_vs_sample.ipynb)

* Defines the `calculate_errors(branching_factor)` function to simulate estimation errors for different branching factors.
* Generates random next-state values from a normal distribution to represent the value distribution.
* Computes the true expected value as the mean of all next-state values.
* Iteratively samples from the distribution to simulate sample-based updates.
* Calculates and stores the absolute difference between the current sample mean and the true value after each update.
* Returns a list of error values showing how the sample mean converges to the true value over time.

[expectation_vs_sample.ipynb](notebooks/expectation_vs_sample.ipynb)

* **Recreates the textbook analysis** comparing *Expected* vs. *Sample* Updates in reinforcement learning.
* **Uses** the `calculate_errors()` function from [`expectation_vs_sample.py`](expectation_vs_sample.py) to simulate **value estimation errors** for various branching factors (`b = 2, 10, 100, 1000`).
* **Runs each experiment 100 times** to average out randomness and produce **smooth learning curves**.
* **Computes and plots** the **Root Mean Square (RMS) error** of the estimated value over **normalized computation time** (`0 → 2b`).
* **Demonstrates** that for large branching factors, **sample updates** reach nearly the same accuracy as **expected updates**, but with far less computation.
* **Saves the resulting visualization** as `figure_8_7.png`, illustrating how sampling becomes more efficient as environments grow more complex.


