### 📌 Gridworld DP Overview (4x4 Grid)

This project applies **Dynamic Programming** techniques to solve a Markov Decision Process (MDP) in a 4×4 grid environment. The goal is to find optimal strategies for an agent navigating toward terminal states.

---

### 🔸 Key Elements

- **Environment**:  
  - 4×4 grid (16 total cells)  
  - 2 terminal states located at corners  
  - Other states transition to neighbors (unless blocked by edges)

- **Available Actions**:  
  - Move up, down, left, or right  
  - Actions are deterministic unless moving off-grid  

- **Rewards**:  
  - Every action gives a reward of **−1**  
  - Terminal states give **0** and end the episode  

- **Policy Type**:  
  - Starts with a uniform random policy (equal chance for each action)  

- **Discount Factor**:  
  - γ = 1.0 (no discounting — future and immediate rewards are equally weighted)

---

### ⚙️ Implemented Algorithms

#### 1. **Iterative Policy Evaluation**
- Estimates the value of each state under the current policy  
- Repeats updates until values stabilize (converge below a small threshold)  
- Terminal states remain fixed at 0  

#### 2. **Policy Improvement**
- Uses the latest value estimates to create a better policy  
- Chooses actions that lead to the highest-valued next state  
- Guaranteed to be equal or better than the previous policy  

---

### 📊 Key Takeaways

- **Convergence**:  
  - Value functions settle around the **negative number of steps to reach terminal states**  
  - Farther cells have lower values (e.g., −14)

- **Update Strategy**:  
  - **In-place** updates: faster but might be less stable  
  - **Out-of-place** updates: more consistent, slower to converge  

- **Policy Learning**:  
  - Even starting from a random policy, a few iterations are enough to find optimal actions  
  - Final policy often includes multiple good choices in some states  

---

### 🧠 Theory Highlights

- **DP Methods Need Full Info**:  
  - These techniques rely on having access to both transition probabilities and rewards

- **Bootstrapping**:  
  - Value updates depend on existing estimates — core idea of DP  

- **Guaranteed Improvement**:  
  - The process of evaluation + improvement ensures progress toward optimal policy

---

