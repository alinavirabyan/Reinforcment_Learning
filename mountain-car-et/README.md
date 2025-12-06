# Sarsa(λ) on the Mountain Car Environment

This project implements and analyzes Sarsa(λ) on the classic Mountain Car control task. The agent must learn to escape a steep valley using momentum rather than direct power, which makes the problem a good demonstration of eligibility traces and function approximation. Tile coding is used to transform the continuous state space into sparse binary features, allowing a simple linear value function to learn effectively.

## Overview

- Implements Sarsa(λ) with several eligibility-trace variants, including accumulating, replacing, Dutch, and replacing-with-clearing.

- Uses tile coding for efficient linear function approximation on continuous states.

- Reproduces experiments similar to those in Reinforcement Learning: An Introduction (Sutton & Barto).

- Generates plots that compare different trace types, step sizes, and λ values.

## Project Structure

- src/mountain_car.py – Environment dynamics, tile-coded Sarsa(λ) agent, eligibility trace rules.

- src/tile_coding.py – Tile coding utilities based on the original Sutton implementations.

- notebooks/mountain_car.ipynb – Main experiment notebook for running learning curves and visualizations.

- generated_images/ – Plots produced during experiments.

- book_images/ – Reference figures reproduced from the textbook.

The structure keeps the agent logic separated from experiment scripts, making it easy to reuse or extend.

## How It Works

- At each step, the agent uses an epsilon-greedy policy (with zero exploration when optimistic initialization is used).

- A tile-coded feature vector maps the state and action to a small set of active indices, keeping learning efficient.

- Eligibility traces ensure that updates flow backward through previously visited state–action pairs.

- The training loop runs multiple episodes and averages results over several independent runs to obtain stable learning curves.

Although the Mountain Car task is simple, the use of eligibility traces demonstrates how Sarsa(λ) can significantly speed up learning in tasks where long-term dependencies matter.

## Running the Experiments

- Install dependencies and open the notebook in notebooks/mountain_car.ipynb.

- Execute the cells that run multiple runs and episodes for each configuration.

- View the generated plots in the generated_images folder.

This produces performance curves that illustrate how trace types and hyperparameters affect early learning efficiency.