# Reinforcement Learning Tic-Tac-Toe

## Overview
This project implements a Reinforcement Learning (RL) agent for playing Tic-Tac-Toe. The RL players are trained using a value-based learning approach, and they can compete against each other or play against a human player.

## Features
- **Train RL players**: Two RL agents learn to play Tic-Tac-Toe using self-play.
- **Compete**: The trained agents can compete against each other with optimal strategies.
- **Human vs AI**: A human player can challenge the trained AI.

## Dependencies
Ensure you have the following Python packages installed:
```bash
pip install numpy
```

## Files & Modules
- `state.py`: Defines board configurations and game states.
- `player.py`: Implements RL and Human players.
- `judge.py`: Handles game rules and matches between players.
- `main.py`: Contains training, competition, and gameplay logic.

## Usage
### Train RL Players
Run the following command to train two RL agents:
```python
python main.py
```
This trains the players for `100,000` epochs and saves their learned policies.

### Compete Between Trained RL Players
Modify `main.py` and call:
```python
compete(turns=1000)
```
This lets the trained players compete and evaluates their performance.

### Play Against AI
To play against the trained RL agent, modify `main.py` and call:
```python
play()
```
You will play as the first player against the RL agent playing second.

## Expected Outputs
- During training, intermediate win rates of both RL agents are printed.
- During competition, the win rates of both RL players are displayed.
- When playing against AI, the game announces if you win, lose, or draw.



