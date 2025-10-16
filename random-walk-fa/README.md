This project explores reinforcement learning using the 1000-state random walk as the environment. It focuses on approximating the value function of states through various methods, including state aggregation, polynomial and Fourier bases, and tile coding. Gradient Monte Carlo and semi-gradient n-step TD algorithms are implemented to update the approximate value functions efficiently. The code evaluates the performance of these methods by measuring RMS errors and comparing approximate values to true state values. Experiments vary parameters such as step sizes, number of episodes, and number of tilings to analyze learning behavior and convergence. Overall, the project demonstrates how different function approximation techniques can generalize learning in large state spaces while balancing accuracy and efficiency.






[**random_walk.py**](./random_walk.py)


* Simulates a **1D random walk** with `states_number` non-terminal states, two terminal states, and random left/right actions.
* Implements **step dynamics** with variable strides, boundary handling, and rewards (-1 for left terminal, +1 for right terminal, 0 otherwise).
* Computes **true state values** using iterative Dynamic Programming (`compute_true_value()`), providing a reference for learning.

#### 🔹 Value Function Approximations

* **Aggregation (`ValueFunction`)**: Groups states and stores one value per group.
* **Polynomial/Fourier (`BasesValueFunction`)**: Uses basis functions to approximate state values.
* **Tile Coding (`TilingsValueFunction`)**: Uses overlapping tilings for efficient state representation.

#### 🔹 Learning Algorithms

* **Gradient Monte Carlo**: Updates parameters using the full episode return.
* **Semi-gradient n-step TD**: Updates parameters online using partial returns with bootstrapping.

#### 🔹 Key Features

* Supports **tabular and function approximation** methods.
* Flexible **step sizes** and trajectory-based updates.
* Designed for **episodic tasks** with evaluation of policy performance.

[**bootstrapping.ipynb**](./bootstrapping.ipynb)

1. **State Aggregation:** Large state spaces (1000 states) are reduced into groups (e.g., 10 or 20) to simplify value function approximation.

2. **Semi-Gradient TD:** Updates state values toward **estimates of next states** (bootstrapping), allowing faster learning than Monte Carlo methods.

3. **n-Step TD:** Generalizes TD(0) by using returns over multiple steps, balancing **bias and variance** in learning.

4. **Left Panel Observation:** TD(0) with 10 groups learns quickly but approximates the true state values slightly less accurately than Monte Carlo.

5. **Right Panel Observation:** n-step TD with 20 groups produces RMS error trends similar to small tabular problems, showing the importance of matching aggregation to transition size.

6. **Takeaway:** TD methods with proper **function approximation** scale to large state spaces, offering faster learning while maintaining accuracy with careful parameter tuning.


[**polynomials_vs_fourier.ipynb**](./random-walk-fa/notebooks/polynomials_vs_fourier.ipynb)

1. **State Aggregation:** Large state spaces (1000 states) are reduced into groups (e.g., 10 or 20) to simplify value function approximation.

2. **Semi-Gradient TD:** Updates state values toward **estimates of next states** (bootstrapping), allowing faster learning than Monte Carlo methods.

3. **n-Step TD:** Generalizes TD(0) by using returns over multiple steps, balancing **bias and variance** in learning.

4. **Left Panel Observation:** TD(0) with 10 groups learns quickly but approximates the true state values slightly less accurately than Monte Carlo.

5. **Right Panel Observation:** n-step TD with 20 groups produces RMS error trends similar to small tabular problems, showing the importance of matching aggregation to transition size.

6. **Takeaway:** TD methods with proper **function approximation** scale to large state spaces, offering faster learning while maintaining accuracy with careful parameter tuning.


[**state_aggregation.ipynb**](./random-walk-fa/notebooks/state_aggregation.ipynb)

1. The notebook demonstrates **state aggregation** in reinforcement learning to simplify large state spaces.
2. It uses the **1000-state random walk** as a test environment to illustrate value function approximation.
3. **Semi-gradient TD(0)** is applied to learn state values efficiently through bootstrapping.
4. The notebook compares TD methods with **Monte Carlo**, showing TD learns faster but may slightly misestimate true values.
5. It explores **n-step TD** with different groupings to balance learning speed and accuracy.
6. The results highlight that **function approximation and proper aggregation** allow TD methods to scale to large state spaces effectively.

[**tile_coding.ipynb**](./random-walk-fa/notebooks/tile_coding.ipynb)

1. The notebook demonstrates **tile coding** as a method of feature representation for large state spaces in reinforcement learning.
2. It applies tile coding to the **1000-state random walk** problem to approximate the value function.
3. Multiple **tilings with offsets** are used to provide overlapping features for better generalization.
4. The notebook shows how **weights for each tile** are updated using semi-gradient TD methods.
5. It compares **different numbers of tilings and tile widths** to analyze their effect on learning performance.
6. Results highlight that **tile coding improves approximation accuracy and learning efficiency** compared to simple state aggregation.


