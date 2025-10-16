# **Model-Based Maze Navigation: Comparing Dyna-Q, Dyna-Q+, and Prioritized Sweeping**

This project explores model-based reinforcement learning in a maze navigation environment using Dyna-Q, Dyna-Q+, and Prioritized Sweeping algorithms. The agent learns to navigate a 6×9 grid with obstacles, starting at a fixed position and aiming to reach a goal while receiving rewards. Dyna-Q combines real experience with simulated planning updates to improve learning efficiency. Dyna-Q+ extends Dyna-Q by adding an exploration bonus, allowing the agent to adapt quickly to changes in the environment. Prioritized Sweeping focuses updates on high-priority state–action pairs, reducing the number of backups needed for efficient learning. Experiments visualize learning curves, show adaptability to maze changes, and highlight how planning and prioritization accelerate model-based reinforcement learning.


[dyna.py](mazes/src/dyna.py)

* Defines the `DynaParams` class as a container for Dyna algorithm parameters.
* `discount` sets the discount factor (γ) for future rewards.
* `exploration_probability` specifies the ε-greedy action selection rate.
* `step_size` determines the learning rate for value updates.
* `time_weight` (κ) adds exploration bonus in Dyna-Q+.
* `planning_steps`, `runs`, `methods`, and `threshold` configure planning steps, number of trials, algorithm names, and priority queue cutoff (θ).

[functions.py](mazes/src/functions.py)

* The `choose_action` function selects an action for the agent using an ε-greedy policy, balancing exploration and exploitation based on the estimated action values.
* The `dyna_q` function executes a single episode of Dyna-Q, updating action-value estimates with real experiences and simulated experiences generated from the model.
* The `changing_maze` function runs experiments where the maze environment changes mid-training, tracking cumulative rewards for different Dyna-based methods and averaging results over multiple runs.
* The `prioritized_sweeping` function implements the Prioritized Sweeping algorithm, focusing planning updates on state-action pairs with the highest priorities to efficiently propagate value updates.
* The `check_path` function evaluates whether the learned policy leads the agent along an approximately optimal path in the maze, returning True if the path length is within a relaxed optimal threshold.
* Overall, the code simulates model-based reinforcement learning in a maze environment, comparing standard Dyna-Q, Dyna-Q+ with exploration bonuses, and Prioritized Sweeping for learning efficiency and adaptability.

[maze.py](mazes/src/maze.py)

* The `Maze` class defines the maze environment, including its size, start state, goal states, obstacles, and possible actions for the agent.
* The constructor initializes the maze dimensions, starting point, goals, obstacles, action-value estimate size, maximum steps, and resolution.
* The `extend_state` method expands a single state into multiple states based on a resolution factor, enabling higher-resolution mazes.
* The `extend_maze` method creates a higher-resolution version of the entire maze, adjusting start, goal, obstacles, and action-value dimensions accordingly.
* The `step` method executes an action in the current state, checks for collisions with obstacles, enforces boundaries, and returns the next state along with the reward.
* Overall, the class provides the foundational environment for Dyna-based reinforcement learning experiments, supporting flexible resolution and dynamic obstacle handling.

[changing_maze.ipynb](mazes/notebooks/changing_maze.ipynb)


* The notebook demonstrates the performance of Dyna-Q and Dyna-Q+ agents in a maze environment where obstacles can change during training.
* It initializes the maze, defines Dyna algorithm parameters, and sets up multiple runs to average results.
* Agents interact with the environment using ε-greedy action selection and update their Q-values with real and simulated experiences.
* Dyna-Q+ includes a time-based exploration bonus that encourages re-exploration after obstacles are moved.
* The notebook tracks cumulative rewards and steps, visualizing the agent’s learning curves before and after the maze changes.
* It highlights how Dyna-Q+ adapts faster to dynamic changes, demonstrating the importance of exploration strategies in model-based reinforcement learning.






[models.py](mazes/src/models.py)
* `TrivialModel` stores state-action transitions and rewards for planning in Dyna-Q; it allows feeding experiences and sampling them randomly.
* `TimeModel` extends `TrivialModel` by including a time-based bonus for unexplored actions, supporting Dyna-Q+ exploration with a small κ-weighted reward adjustment.
* `PriorityQueue` implements a min-heap priority queue with methods to add, remove, and pop items, while handling duplicates and empty queue cases.
* `PriorityModel` extends `TrivialModel` for Prioritized Sweeping by maintaining a priority queue and tracking predecessors for efficient backward updates.
* In `PriorityModel`, `insert()` adds state-action pairs to the queue with negative priority (max-heap behavior), `sample()` retrieves the top-priority item, and `predecessor()` returns all predecessors for a given state.
* These classes collectively support Dyna-Q, Dyna-Q+, and Prioritized Sweeping algorithms for model-based reinforcement learning in maze environments.

[dyna_maze.ipynb](mazes/notebooks/dyna_maze.ipynb)

* This code reproduces the experiment from Figure 8.2, showing how Dyna-Q agents learn in a 47-state maze.
* It sets up a maze (`dyna_maze`) and Dyna algorithm parameters (`dyna_params`) including discount rate, exploration probability, and step-size.
* Three different numbers of planning steps (`0, 5, 50`) are tested to compare how planning accelerates learning.
* For each run and each episode, the agent uses the `dyna_q` function to interact with the maze, update Q-values, and perform simulated planning steps.
* The steps taken to reach the goal in each episode are averaged over 10 runs to reduce randomness.
* Finally, the learning curves (steps vs. episodes) are plotted, showing that more planning steps significantly improve learning speed, matching the observations in the book.

[prioritized_sweeping.ipynb](mazes/notebooks/prioritized_sweeping.ipynb)


1. The code compares **Prioritized Sweeping** and **Dyna-Q** on a sequence of mazes of increasing resolution, tracking how quickly each method finds the optimal solution.
2. It first creates the original 6×9 maze and sets the corresponding Dyna-Q and Prioritized Sweeping parameters, including planning steps, step size, discount factor, and priority threshold.
3. Multiple mazes are generated by increasing the grid resolution, with each new maze having more states than the previous one.
4. For each run, method, and maze, the code initializes Q-values and a model, then repeatedly applies the selected planning algorithm until the optimal path is found.
5. The total number of backups (state-action updates) required to find the optimal solution is recorded for each maze, averaged across multiple runs, and scaled for Dyna-Q to account for planning steps.
6. Finally, the results are plotted on a logarithmic scale to compare how the number of backups grows with maze resolution for both methods, showing the efficiency advantage of Prioritized Sweeping.
