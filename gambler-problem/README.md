### 📌 Gambler's Problem Overview

The **Gambler’s Problem** is a classic example of a Markov Decision Process (MDP) where an agent (the gambler) tries to reach a target amount of money by placing bets. The problem involves decision-making under uncertainty with rewards depending on probabilistic outcomes.

---

### 🔸 Key Components

- **State Space (S)**:  
  - Represents the gambler’s current amount of money  
  - States range from 0 to the target amount (e.g., 100 dollars)  

- **Action Space (A)**:  
  - The gambler can bet a certain amount of money each time (typically 1 or more dollars)

- **Reward Function**:  
  - **+1** reward for reaching the target (e.g., 100 dollars)  
  - **−1** reward for going broke (0 dollars)  
  - No reward for other transitions

- **Transition Model**:  
  - The gambler wins or loses the bet based on a 50/50 chance  
  - Probabilities:  
    - Win: 0.5  
    - Lose: 0.5

- **Discount Factor (γ)**:  
  - Typically set to **1** (future rewards are as important as immediate rewards)

---

### ⚙️ Problem Setup

- **Goal**:  
  - The objective is to find the optimal betting strategy to maximize the chance of reaching the target amount without going broke.

- **Terminal States**:  
  - **0 dollars** (game over — broke)  
  - **Target amount** (game over — win)

---

### 🧠 Methods Used to Solve

#### 1. **Value Iteration**
- Iteratively updates the value of each state by considering all possible actions and transitions  
- The value of each state represents the expected reward starting from that state  
- Converges to the optimal value function, which tells the gambler the best expected outcome for any given state

#### 2. **Policy Iteration**
- Alternates between evaluating the current policy and improving it  
- Starts with a random policy and improves it iteratively  
- Leads to the optimal betting strategy (policy) that maximizes the gambler’s chances of success

---

### 📊 Key Insights

- **Dynamic Programming**:  
  - Requires the gambler to know the full transition probabilities (model-based approach)  
  - Uses **Bellman equations** to calculate values and improve policies
  
- **Optimal Policy**:  
  - The optimal policy is the strategy that maximizes the expected probability of reaching the target amount without going broke  
  - It may suggest that the gambler should bet more when they have a higher chance of winning and bet less when they’re closer to going broke

- **Exploration of States**:  
  - States closer to 0 dollars have lower values because they carry a higher risk of losing all the money

---

### 💡 Theoretical Implications

- **MDP Representation**:  
  - The problem is a typical MDP where the agent (gambler) must choose actions (bets) to reach a goal (target amount) while avoiding a losing state (broke)  

- **Value Iteration vs. Policy Iteration**:  
  - **Value Iteration**: Works by updating values based on the Bellman equation until convergence  
  - **Policy Iteration**: Alternates between policy evaluation and improvement, ensuring that the resulting policy is optimal

- **Real-World Applications**:  
  - Though framed as a gambling problem, it illustrates concepts in decision-making, risk management, and optimization problems, with applications in finance, robotics, and resource allocation.

---
