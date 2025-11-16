# On-policy Control with Approximation — Access-Control Queue Example

This project demonstrates **average-reward on-policy control** using **differential semi-gradient Sarsa** applied to the **Access-Control Queue** task from Sutton & Barto (Reinforcement Learning, Chapter 10).

The goal is to learn a policy that decides whether to **accept or reject** incoming customers of different priority levels when server capacity is limited, in order to maximize the long-term average reward. Although the implementation is **tabular**, it naturally fits within the **function approximation framework**, where each state–action pair has its own differential value estimate.

---

## Description

This example shows how to perform **on-policy control** in a **continuing task** where discounting is not suitable. Instead of maximizing discounted return, the objective is to maximize the **average reward per time step**.

We apply **differential semi-gradient Sarsa** to the Access-Control Queue problem:

- **Environment:** an infinite queue of customers with random priorities  
- **Servers:** 10 servers that become free unpredictably  
- **Actions:** accept or reject the next customer in line  
- **Reward:** equal to the customer's priority when accepted, otherwise 0  
- **Objective:** improve the policy toward higher long-term average reward  

Even though the implementation is tabular, each state–action pair can be treated as a feature vector, making this a **special case of linear function approximation**.

---

## Problem Formulation

This is a **continuing, undiscounted** reinforcement-learning setting. Because the process never ends, using discounting biases the outcome toward early rewards. The **average-reward** formulation avoids this issue and evaluates performance based on the long-run average reward.

### State Space

A state is represented by:

- Number of free servers: `0–10`  
- Priority of the next customer: `{1, 2, 4, 8}`

### Actions

- **Accept** — allocate the customer to a server  
- **Reject** — decline the customer and gain no reward  
  *(Rejection is forced when no servers are free)*

### Rewards

- Accepting a customer yields reward equal to their priority  
- Rejecting a customer yields 0  

### Transitions

- Busy servers become free with a fixed probability each time step  
- Customer priorities are uniformly random  
- The queue is never empty  

### Why Average-Reward RL?

Since the system never terminates, discounting introduces an undesired emphasis on short-term gains. The average-reward objective focuses on long-run performance by comparing each action to the ongoing reward baseline rather than a discounted return.

---

## Methodology

### Algorithm

- **Differential Semi-gradient Sarsa**  
- On-policy control with ε-greedy exploration  
- Maintains and updates an estimate of the **average reward**  
- Updates action-value estimates based on the change relative to this average  

### Policy

ε-greedy with respect to the differential action-value estimates ensures that the agent continues to explore while gradually improving the policy.

### Relation to Function Approximation

Although implemented as a table, each state–action can be encoded as a feature vector. This means the example directly maps to **linear function approximation**, and the same approach can scale to larger access-control systems by expanding the feature representation.

---

## Parameters

The following parameters match the setup described in Sutton & Barto:

| Parameter | Value |
|-----------|--------|
| α (step size for q) | 0.01 |
| β (step size for average reward) | 0.01 |
| ε (epsilon-greedy) | 0.1 |
| Servers | 10 |
| Priorities | {1, 2, 4, 8} |
| Server-free probability | 0.06 |
| Initial q-values | 0 |
| Initial average reward | 0 |

---

## Results

### Learned Policy

After training, the agent learns a strategy that:

- **rejects low-priority customers when server capacity is low**
- **accepts nearly all customers when many servers are free**
- is conservative with low priorities (1 and 2), and more eager to accept priorities 4 and 8

This reflects a reasonable balance between preserving resources for high-value customers and utilizing available capacity.

### Differential Value Estimates

Key observations from the learned value function:

- The estimated average reward converges to around **2.31**
- High-priority customers and states with many free servers show the most positive value estimates
- Some rarely visited states (e.g., 9–10 free servers with low-priority customers) have less accurate estimates due to low visitation frequency

---

## Generated Figures

The notebook includes visualizations such as:

- **Policy Heatmap:** shows accept/reject actions across (free servers × priority)
- **Differential Value Estimates:** illustrates the action-value landscape

These plots provide insight into both the learned behaviour and value predictions.

---
