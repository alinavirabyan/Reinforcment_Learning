import numpy as np

# region Hyper-parameters

# Number of states
states_number = 19

# Discount rate (denoted as 𝛾)
discount = 1

# Non-terminal states
non_terminal_states = np.arange(1, states_number + 1)

# Terminal states. An action leading to the:
#                                           left terminal state has reward -1,
#                                           right terminal state has reward 1.
terminal_states = [0, states_number + 1]

# True state-values of non-terminal states from Bellman equation
true_state_values = np.arange(-20, 22, 2) / 20.0

# True state-values of terminal states
true_state_values[0] = true_state_values[-1] = 0

# Start from the middle state
start = 10

# endregion Hyper-parameters

# region Functions

def temporal_difference(state_value_estimates, steps_number, step_size):
    # region Summary
    """
    n-steps TD Method
    :param state_value_estimates: Value estimates for each state (denoted as V)
    :param steps_number: Number of steps (denoted as n)
    :param step_size: Step-size parameter (denoted as 𝛼)
    """
    # endregion Summary

    # region Body

    # Initialize starting state


    # List to store states for an episode


    # List to store rewards for an episode


    # Track the time


    # Define the length of this episode



        # Move to next time step


        # If the episode is not over

            # choose an action randomly



            # check the left terminal state


            # check the right terminal state


            # reward for all non-terminal states is 0


            # store the new state


            # store the new reward


            # check terminal states


        # Get the time of the state to update




            # Calculate corresponding returns (Equation (7.1)):


            # If episode is not over

                # add state-value estimate to the return (Equation (7.1)):


            # Get the state to update


            # If state to be updated is a non-terminal state

                # update the state-value estimate (Equation (7.2)):


        # If episode is over


        # Move to the next state


    # endregion Body

# endregion Functions
