### 🌍 Grid-World MDP Overview

This project explores how decision-making works in a simple 5x5 grid using Markov Decision Processes (MDPs). It focuses on finding the best actions an agent can take using two main methods: policy evaluation and value iteration.

---

### 🔹 Main Concepts

- **States**: Each cell in the 5x5 grid (25 total).
- **Actions**: Move up, down, left, or right.
- **Rewards**:  
  - Special cells (A → A′ gives +10, B → B′ gives +5)  
  - Hitting walls gives −1  
  - Other moves give 0
- **Transitions**: Actions usually work as expected, unless hitting grid edges.
- **Discount Factor (γ = 0.9)**: Balances short-term and long-term rewards.

---

### 🛠 Algorithms Used

#### 1. **Policy Evaluation**
- Calculates the value of each state when following a random policy.
- Helps understand how good it is to be in a state under that policy.

#### 2. **Value Iteration**
- Finds the best value for each state by choosing the best action.
- After values settle, the best actions form the optimal policy.

---

### 📈 What We Learn

- Edge states usually have lower value due to penalties.
- Smart action choices can increase a state's value beyond its direct reward.
- MDPs help model decision-making by combining rewards, future outcomes, and strategy.

---
