#  Coarse Coding — Square Wave Example

This project demonstrates the effect of **receptive field size** (feature width) on learning within **coarse coding** using **linear function approximation**.  
The goal is to learn a **1-dimensional square-wave function** with different receptive field widths and observe how generalization changes.


---

##  Description

This example illustrates the **Coarseness of Coarse Coding** — specifically, how the **width of receptive fields** affects learning and generalization.

Linear function approximation is applied to learn a 1D square-wave target function.  
Each receptive field corresponds to an **interval** (since the input is 1D).  
The experiment compares **three widths**:

- Narrow features → fine, bumpy learning
- Medium features → balanced generalization
- Broad features → smooth but slower convergence

All configurations use the same feature density (~50 features).

---

##  Methodology

- **Algorithm:** Linear function approximation (Equation 9.7)
- **Feature widths tested:** 0.2, 0.4, 1.0  
- **Sample sizes:** 10, 40, 160, 640, 2560, 10240  
- **Training data:** Random samples uniformly distributed across the domain  
- **Visualization:** Plots of learned functions after training

---

## Source Files Overview
**classes.py**

Defines:

- DOMAIN: defines the range of the function

- ValueFunction: implements the linear approximation based on coarse coding

**square_wave.py**

Includes:

- sample(): generates random training samples

- approximate(): trains a ValueFunction based on provided samples
---

**notebooks/square_wave.ipynb**

The notebook performs the main experiment:

- Loads helper modules from src/.

- Trains three models with different feature widths (0.2, 0.4, 1.0).

- Repeats training for different sample sizes (10 → 10240).

- Plots approximations to visualize the effect of feature coarseness.

> Output plot is saved as:
  generated_images/figure_9_8.png
