# Random Walk — Eligibility Traces  
### Off-line λ-return • TD(λ) • True Online TD(λ)

This project implements and reproduces experiments from **Chapter 12** of *Sutton & Barto (2018), Reinforcement Learning: An Introduction (2nd Edition)*, focusing on value prediction with **eligibility traces**.  
The classical **19-state random walk** task is used to compare different λ-based algorithms and analyze their learning behavior under varying parameters.

The primary goals of this project are:

- Implementing off-line λ-return (forward view)
- Implementing TD(λ) (backward view)
- Implementing True Online TD(λ) (online λ-return)
- Running parameter sweeps over α and λ
- Reproducing Figures **12.3**, **12.6**, and **12.8** from the textbook


---

##  Background: Eligibility Traces

Eligibility traces provide a bridge between Monte Carlo methods and TD(0).  
They act as short-term memory, determining how much previous states should be updated based on what happens later in the episode.

This project compares three major approaches:

### **1. Off-line λ-return (Forward View)**
- Computes the λ-return after the entire episode.
- Provides the exact forward-view update target.
- Accurate but computationally expensive for long episodes.

### **2. TD(λ) (Backward View)**
- Uses accumulating eligibility traces.
- Updates weights online using the TD error.
- Efficient but only approximates the forward-view behavior.

### **3. True Online TD(λ)**
- Implements the corrected “Dutch trace.”
- Fully online method that matches the forward view for linear function approximation.
- More stable and accurate during online learning.

---

##  Experimental Setup

### **Random Walk Environment**
- 19 non-terminal states.
- Terminal states on the left and right.
- Reward of +1 on the right terminal; 0 elsewhere.
- Episodes begin in the middle.
- Each step moves the agent randomly left or right.

### **Experiment Parameters**
- **Runs:** 50  
- **Episodes per run:** 10  
- **Discount factor (γ):** 1.0  
- **Evaluated λ values:**  
  0.0, 0.4, 0.8, 0.9, 0.95, 0.975, 0.99, 1.0  
- **Performance metric:** RMS error between predicted and true values.

### **Figures Produced**
Saved automatically in `generated_images/`:


Each figure plots RMS error versus α for multiple λ values, replicating the textbook’s results.

---

##  Implementation Overview

The core implementation resides in `src/random_walk.py`:

- **OffLineLambdaReturn**  
  Stores transitions and performs updates after episodes.

- **TDLambda**  
  Classical backward-view algorithm with accumulating traces.

- **TrueOnlineTDLambda**  
  Implements Dutch traces and online updates consistent with the forward view.

- **parameter_sweep**  
  Automates running multiple algorithms across different α and λ values and generating the corresponding plots.

---


