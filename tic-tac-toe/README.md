### 🎮 **Tic-Tac-Toe and Reinforcement Learning – Key Points:**

1. 🟦 **Game Overview**:  
   Played on a 3x3 board. Two players (X and O) take turns. Win by getting three in a row. A full board with no winner is a draw.

2. 🤖 **Assumption for Learning**:  
   Opponent is imperfect. Only wins matter — draws and losses are equally bad.

3. ⚠️ **Challenges with Classical Methods**:  
   - **Minimax** assumes perfect play — not suitable here.  
   - **Dynamic Programming** requires full opponent model — impractical.

4. 🧬 **Evolutionary Methods (Alternative)**:  
   - Try many policies (move rules) and evolve better ones.  
   - Evaluate by game outcomes, not individual moves.

5. 🔁 **Reinforcement Learning Approach**:  
   - Learns value of each board state.  
   - Value = chance of winning from that state.  
   - Start: 1 (win), 0 (loss/draw), 0.5 (unknown).  
   - Learns by playing many games.

6. 🎯 **Move Selection**:  
   - Mostly **greedy** (choose highest value move).  
   - Sometimes **exploratory** (random move) to find new paths.

7. 📈 **Learning from Moves**:  
   - After greedy moves, update state values using **Temporal-Difference (TD) Learning**:  
     `V(St) = V(St) + α [V(St+1) - V(St)]`

8. 🧪 **Exploratory vs. Greedy Moves**:  
   - Exploratory = no learning (just trying new moves).  
   - Greedy = causes learning via updates.

9. 🚀 **Benefits of This Method**:  
   - Learns optimal play against imperfect opponents.  
   - Adapts over time.  
   - No need to model the opponent.

10. 🧠 **Generalization**:  
    - Works for more complex games too (like backgammon).  
    - Use neural networks when state space is huge.

