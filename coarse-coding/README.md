**Coarse Coding**


[classes.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/coarse-coding/src/classes.py)

* Defines an **Interval** class to represent a range and check whether a point lies within it.
* `ValueFunction` class approximates values using **overlapping feature windows** over a continuous domain.
* Each feature window is represented by an `Interval` and has an associated **weight**.
* `value(point)` estimates the value of a point by summing the weights of all **active features** containing it.
* `update(delta, point)` adjusts the weights of active features for **learning** using a step-size parameter.

[square_wave.py](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/coarse-coding/src/square_wave.py)

* Defines a **square wave function** over the domain [0, 2), returning 1 in (0.5, 1.5) and 0 elsewhere.
* `sample(n)` draws `n` random points from the domain and evaluates the square wave to generate training samples.
* `approximate(samples, value_function)` trains a `ValueFunction` using the generated samples.
* Updates are based on the **difference between true square wave values and current VF estimates**.
* Supports **function approximation with overlapping feature windows** for continuous domains.

[square_wave.ipynb](https://github.com/alinavirabyan/Reinforcment_Learning/blob/main/coarse-coding/notebooks/square_wave.ipynb)

* Demonstrates **coarse coding** and its effect on learning a 1D square-wave function.
* Uses **linear function approximation** with feature intervals of different widths: narrow, medium, and broad.
* Training samples are drawn uniformly at random, and step size is adjusted by the number of active features.
* **Feature width strongly affects early learning**: broad features generalize widely, narrow features produce bumpy approximations.
* Final learned function is only slightly affected by feature width, showing **receptive field shape affects generalization, not asymptotic solution quality**.
