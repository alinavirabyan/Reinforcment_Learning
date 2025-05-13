**WINDY-GRIDWORLD IMPLEMENTATION**

The Windy Gridworld is a grid-based environment where an agent must navigate from a start state to a goal state. Unlike a regular grid, certain columns have a vertical wind effect that pushes the agent upward, making the environment more challenging. The agent receives a reward of -1 for each step until it reaches the goal, encouraging it to find the shortest path. The task is solved using the SARSA algorithm with ε-greedy action selection to learn the optimal path over time.

The project consists of the following files:

[windy_grid_world.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/windy-gridworld/notebooks/windy_grid_world.ipynb):

- Initialized a 3D array to store action-value estimates for all grid states and actions.

- Ran 170 episodes using the play() function, which executed SARSA to update the action-value estimates.

- Tracked the total number of time steps taken per episode and accumulated them for plotting.

- Plotted the relationship between total time steps and number of episodes to show learning progress.

- Extracted the optimal policy from the learned action-value estimates by choosing the best action at each state.

- Displayed the optimal policy as arrows indicating direction and printed the wind strength for each column

[windy_grid_world.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/windy-gridworld/src/windy_grid_world.py):


- The code sets up the **Windy Gridworld environment**, where an agent starts at a given position and must reach a goal, facing vertical wind in certain columns that pushes it upwards.
  
-  The `step` function determines the **next position** of the agent based on the chosen action and the wind strength in the current column.
  
- The `choose_action` function implements an **ε-greedy strategy**, which selects a random action with probability ε or the best-known action (highest Q-value) otherwise.
  
- The `play` function runs a **single episode** where the agent moves from the start state to the goal using the SARSA algorithm.
  
- At each step, SARSA updates the **action-value estimate** (Q-value) using the current state, action, reward, next state, and next action.
  
- The Q-values are stored in a 3D array where each cell corresponds to a state and action, and they get updated during learning.
  
- The loop continues until the agent reaches the goal, and the function returns the number of steps (time steps) it took to finish the episode.

