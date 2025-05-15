# **GRIDWORLD IMPLEMENTATION WITH MARKOV DECISION PROCESS**

A **Markov Decision Process (MDP)** is a mathematical framework used to model decision-making in environments where outcomes are partly random and partly under the control of an agent. MDPs are widely used in reinforcement learning.
An MDP consists of the following key components:

1. **States (S):**
   A finite set of states that fully describe the environment at any given time. Each state represents a possible situation the agent can be in.

2. **Actions (A):**
   A finite set of actions available to the agent. The set of actions available can depend on the current state, but in many cases, all actions are available in all states.

3. **Transition Function (T):**
   A probabilistic function that defines the likelihood of transitioning from one state to another, given a specific action.

   * $T(s, a, s') = P(s_{t+1} = s' \mid s_t = s, a_t = a)$
     This function satisfies the **Markov property**, meaning the next state depends only on the current state and action, not the full history.

4. **Reward Function (R):**
   A function that assigns a numeric reward for taking an action in a state or for transitioning from one state to another.
   Common forms include:

   * $R(s)$: reward for being in state $s$
   * $R(s, a)$: reward for taking action $a$ in state $s$
   * $R(s, a, s')$: reward for transitioning from $s$ to $s'$ via $a$

5. **Policy (π):**
   A strategy that defines the action the agent takes in each state. The goal of the agent is to learn an optimal policy that maximizes cumulative future rewards.

6. **Initial State Distribution (I):**
   A probability distribution that defines where episodes start (used in episodic tasks).

7. **Goal States and Episodes:**
   In **episodic tasks**, there are terminal or absorbing states where the process ends. Upon reaching a goal, the system resets to a new start state.



###  **Types of MDP Tasks:**

* **Finite-horizon:** Episodes have a fixed number of steps.
* **Indefinite-horizon:** Episodes can vary in length.
* **Infinite-horizon / Continuing tasks:** The process never ends.


###  **Absorbing States:**

Absorbing states are states where any action leads back to the same state with zero reward, modeling the end of an episode:
* $T(s, a, s) = 1$ and $R(s, a, s') = 0$

### **Goals and rewards**
In reinforcement learning, the agent’s goal is formalized through a reward signal from the environment, which it aims to maximize over time. This reward hypothesis states that all goals can be represented as maximizing the expected cumulative reward. The reward signal guides the agent toward desired behaviors without specifying how to achieve them, allowing flexibility in learning. It is crucial to design rewards carefully so that maximizing them aligns with the true goals, avoiding unintended behaviors.

### **Returns and episodes**

The agent’s goal in reinforcement learning is to maximize the expected return, which is a function of the sequence of future rewards. In episodic tasks, the return is the sum of rewards until a terminal state ends the episode, while continuing tasks have no natural end and require a different approach. To handle continuing tasks, rewards are discounted over time using a discount rate, which reduces the value of future rewards compared to immediate ones. The discount rate determines how farsighted the agent is, with lower values making it focus more on immediate rewards and higher values valuing future rewards more. Returns at successive time steps relate recursively, allowing easier computation, and the discounted return remains finite even with an infinite sequence of rewards if the discount rate is less than one.


### **Policies and Value Functions**

Reinforcement learning algorithms estimate value functions that predict how good it is for an agent to be in a state or take an action, based on expected future rewards. These value functions depend on the agent’s policy, which maps states to action probabilities. The state-value function $v_\pi(s)$ gives the expected return starting from state $s$ following policy $\pi$, while the action-value function $q_\pi(s,a)$ gives the expected return starting from state $s$, taking action $a$, then following $\pi$.
Value functions satisfy the Bellman equation, which expresses a recursive relationship: the value of a state equals the expected immediate reward plus the discounted value of successor states. This equation forms the foundation for many reinforcement learning methods.
An example gridworld MDP illustrates these ideas, where the agent moves on a grid, receives rewards based on actions, and the value function reflects the expected discounted returns under a given policy.


### **Optimal Policies and Optimal Value Functions**

Solving a reinforcement learning task means finding the best way to act to get the most reward over time. One policy is better than another if it gives more reward in every situation. An optimal policy is the best possible one—it gives the highest rewards. All optimal policies lead to the same results in the long run. These results are described by the optimal value functions, which tell us how good it is to be in a state or to take a certain action. The value of taking an action in a state depends on the reward you get right away and the value of the next state you end up in.

The project consists of the following file:

[grid_world.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gridworld-mdp/notebooks/grid_world.ipynb)

1. **Initialize State Values**: A table of zeros (`state_values`) is created to store value estimates for each state in the grid.

2. **Random Policy Evaluation**: For the first part, the agent evaluates a random policy (equal probability for each action), updating state values using the Bellman expectation equation.

3. **Loop Until Convergence**: The algorithm iteratively updates state values until the difference between updates becomes very small (less than `1e-4`).

4. **Value Iteration for Optimal Policy**: In the second part, the algorithm computes the optimal value function by applying the Bellman *optimality* equation, selecting the best action for each state.

5. **Track Best Actions**: For each state, the code calculates possible action outcomes and chooses the one yielding the maximum value.

6. **Save Visual Results**: Once the values converge, the results are visualized and saved as images showing the optimal value function and corresponding optimal policy.


[grid_world.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/gridworld-mdp/src/grid_world.py)


1. A 5x5 gridworld is defined with two special states (A and B), which teleport the agent to A′ and B′ respectively, with rewards of +10 and +5.
2. The agent can take four possible actions (left, up, right, down), and the `step` function determines the next state and reward for a given action.
3. If the action would move the agent off the grid, the agent stays in place and receives a reward of -1.
4. The `draw` function visualizes either the state-value function or the optimal policy for the grid.
5. When visualizing a policy, the function simulates all possible actions from each state and highlights the direction(s) that lead to the highest value.
6. Special states A, A′, B, and B′ are labeled clearly in the grid for easy recognition.
7. The grid visualization is built using `matplotlib` tables, with cell arrows indicating optimal actions where applicable.


Comparison with Sutton's Book Output
This implementation was inspired by Gridworld Example 3.8 from "Reinforcement Learning: An Introduction" by Sutton & Barto. Below is a comparison of the results:

[Sutton's Book Output](https://github.com/alinavirabyan/Reinforcment_Learning/tree/main/gridworld-mdp/book_images)


![image](https://github.com/user-attachments/assets/a66408f7-433e-4775-9c78-8e35eba28fe2)

![image](https://github.com/user-attachments/assets/e6cc308f-2d95-45e9-ac06-0a7128e15b6e)

[ My Code Output](https://github.com/alinavirabyan/Reinforcment_Learning/tree/main/gridworld-mdp/generated_images)

 
![image](https://github.com/user-attachments/assets/e0fe2f15-87c3-4d7a-a09e-8ac6fc105e32)

![image](https://github.com/user-attachments/assets/0fabf34c-3eae-4029-ae2a-0175bc7317a4)

![image](https://github.com/user-attachments/assets/ede76a2b-7213-427d-bb0f-7c0267901dbc)




