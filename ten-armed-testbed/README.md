🎰 **What is the 10-Armed Bandit Problem?**  
- 🎯 A basic problem in reinforcement learning.  
- 🕹️ You choose from **10 actions (arms)** repeatedly.  
- 💰 Each action gives a **random reward** based on an unknown distribution.  
- 🧠 The goal is to **maximize total reward** over time.

---

🔍 **Key Concepts**  
- 📊 **Evaluative Feedback**: You learn only from rewards, not from being told the right action.  
- ⚖️ **Exploration vs Exploitation**:  
  - 🚀 *Exploration*: Try new actions to discover their value.  
  - 💎 *Exploitation*: Use the best-known action to get rewards.

---

🧮 **How to Estimate Action Values**  
- ➕ Take the **average** of the rewards received from each action.  
- 🟢 **Greedy method**: Always pick the action with the highest current value.  
- 🔁 **ε-Greedy method**:  
  - 💡 Choose a random action **ε%** of the time.  
  - ✅ Choose the best-known action **(1 - ε)%** of the time.

---

🧪 **10-Armed Testbed Experiment**  
- 🔢 Run on **2000 random problems**.  
- 📈 ε-Greedy (with ε = 0.1 or 0.01) performed **better than greedy**, because:  
  - 🌱 They explored more.  
  - 🧠 Found better actions over time.

