**RANDOM-WALK-ET**

[random_walk.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/random-walk-et/src/random_walk.py)
1. This code implements three λ-based value function learning algorithms for a 19-state random walk.
2. `ValueFunction` is the base class; `OffLineLambdaReturn`, `TemporalDifferenceLambda`, and `OnLineLambdaReturn` are derived classes.
3. `OffLineLambdaReturn` updates weights **after each episode** using λ-returns.
4. `TemporalDifferenceLambda` updates weights **online** using TD error and accumulating eligibility traces.
5. `OnLineLambdaReturn` implements true online TD(λ) with Dutch traces for more precise updates.
6. `random_walk` simulates episodes where the agent moves left or right until reaching terminal states (-1 or +1 reward).
7. `parameter_sweep` tests different λ and α values, calculates RMSE against true state values, and plots learning performance.

[random_walk.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/random-walk-et/notebooks/random_walk.ipynb)
1. This code compares **off-line λ-return**, **TD(λ)**, and **online λ-return** algorithms on a 19-state random walk.
2. Off-line λ-return updates weights only at the **end of each episode**, blending Monte Carlo and one-step TD methods.
3. TD(λ) updates weights **online** using accumulating eligibility traces and TD errors, approximating the off-line λ-return.
4. Online λ-return (true online TD) updates weights at **every step** during the episode, making it more computationally intensive but often more accurate.
5. `parameter_sweep` runs multiple episodes with different λ (trace-decay) and α (step-size) values, calculating **RMSE** against true state values.
6. Experiments show intermediate λ values give the best performance for both off-line and TD(λ) methods; online λ-return generally outperforms off-line during and after episodes.
7. Results are visualized in figures, saved as PNGs (`figure_12_3.png`, `figure_12_6.png`, `figure_12_8.png`) to compare algorithm performance.
