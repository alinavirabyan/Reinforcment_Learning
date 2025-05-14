# **BLACKJACK PROBLEM IMPLEMENTATION**

Monte Carlo methods learn value functions and optimal policies from sample episodes without needing a model of the environment, making them suitable for direct learning from experience. Unlike dynamic programming (DP), they do not bootstrap, meaning they update value estimates based solely on actual returns rather than estimated future values. They support efficient learning in specific state regions, allow for on-policy and off-policy learning, and require strategies to ensure sufficient exploration.
Monte Carlo methods are often demonstrated using the **game of blackjack**, where they can effectively learn optimal strategies by simulating many episodes and averaging returns for different state–action pairs.

The project consists of the following files:

 [black_jack.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/blackjack/notebooks/black_jack.ipynb)

1. Defined the Environment

- Blackjack is framed as a finite MDP with episodes ending in win/loss/draw.

- States include:

   - Player’s current sum (12–21)
   - Dealer’s visible card (1–10)
   - Whether the player has a usable ace

- Rewards are:

    - +1 (win)
    - -1 (lose)
    - 0 (draw)

2. Monte Carlo Policy Evaluation
   

- Simulated games using a fixed policy (stick at 20 or 21).
- Used sample-averaged returns to estimate state values.
- Visualized state-value functions with and without usable ace (Figure 5.1).


3. Monte Carlo Control (Exploring Starts)


- Found optimal policy using MC-ES.
- Updated action-value functions and derived state-values and greedy policies.
- Produced visualizations showing optimal policy and value (Figure 5.2).


4. (Attempted) Off-policy Prediction via Importance Sampling
   

- Evaluating the value of a single state: (usable ace, player sum 13, dealer shows 2).
- Preparing to use importance sampling.


[black_jack.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/blackjack/src/black_jack.py)


1. This code simulates the game of Blackjack using Monte Carlo methods to evaluate a player's strategy.
2. It defines player and dealer policies, where the player hits below 20 and the dealer sticks at 17 or higher.
3. The `play` function executes a single game, tracking player and dealer actions and determining the reward.
4. Helper functions handle card values, updates, and checking for usable aces to simulate realistic gameplay.
5. The `monte_carlo_on_policy` function runs many games to estimate expected returns for each state using the player's policy.
6. Results are stored separately for cases with and without a usable ace to compare their impact on performance.


