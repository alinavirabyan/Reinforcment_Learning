**Counter-examples**

* Demonstrates **off-policy divergence** in semi-gradient TD with linear function approximation.
* Environment: 7 states (6 upper, 1 lower) and 2 actions (dashed for upper, solid for lower).
* Behavior policy: mostly dashed (6/7) vs. target policy: always solid; rewards are 0 and discount factor γ = 0.99.
* Semi-gradient TD updates weights to approximate state values; both step-by-step and DP-style updates diverge.
* Highlights the need for **Gradient-TD or Emphatic-TD methods** for stable off-policy learning.

[counter-example.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/counter-examples/src/counter_example.py)

* The environment consists of 7 states (6 upper, 1 lower) with 2 actions: dashed (upper) and solid (lower), using feature vectors of length 8 to represent states.
* Behavior policy mostly selects dashed (6/7) while the target policy always selects solid; rewards are zero and the discount factor is γ = 0.99.
* Semi-gradient off-policy TD updates weights using importance sampling and TD errors, which leads to divergence even under linear function approximation.
* Semi-gradient DP performs expected updates across all states, but divergence persists, confirming theoretical instability.
* Gradient-TD (TDC) and Emphatic-TD methods are implemented to provide stable off-policy learning by correcting the updates with auxiliary weights or emphases.

[bairds_counterexample.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/counter-examples/notebooks/bairds_counterexample.ipynb)

1. This code implements Baird’s Counterexample, illustrating divergence in semi-gradient off-policy TD learning for a 7-state, 2-action MDP.
2. It initializes feature vectors for each state and sets up the weights, step size, and number of steps or sweeps for the experiments.
3. The first part simulates semi-gradient off-policy TD, updating weights step by step while recording their evolution in a matrix.
4. The second part runs a semi-gradient DP update synchronously across all states, again tracking weights over time.
5. Finally, the code plots the evolution of all weights for both methods and saves the figure, showing divergence as expected in Baird’s counterexample.

[emphatic_baird.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/counter-examples/notebooks/emphatic_baird.ipynb)

1. This code implements the Expected Emphatic-TD algorithm for Baird’s counterexample, tracking the expected trajectory of the weight vector.
2. It initializes the weights, step size, number of sweeps, and emphasis, and prepares matrices to record the weights and RMS-VE over time.
3. For each sweep, it updates the weights and emphasis using the expected Emphatic-TD method and calculates the RMS Value Error.
4. The code captures the evolution of each weight component as well as the overall RMS-VE to visualize convergence.
5. Finally, it plots and saves the results, showing that despite some oscillations, the method converges in expectation, unlike standard semi-gradient off-policy TD.

[tdc_baird.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/counter-examples/notebooks/tdc_baird.ipynb)

1. This code implements the TDC (TD(0) with gradient correction) algorithm and its expected variant on Baird’s counterexample.
2. It initializes weights, the linear least-squares (LLS) solution vector, step sizes for weights and LLS, and arrays to track RMS-VE and RMS-PBE over iterations.
3. For each step (or sweep), it updates the weights and LLS solution using the TDC or expected TDC algorithm and records the current weights.
4. The code also calculates the Root Mean Square Value Error (RMS-VE) and the Root Mean Square Projected Bellman Error (RMS-PBE) to monitor learning progress.
5. Finally, it plots the evolution of all weight components, RMS-VE, and RMS-PBE, showing slow convergence toward the optimal solution with some weights remaining far from their target values.












