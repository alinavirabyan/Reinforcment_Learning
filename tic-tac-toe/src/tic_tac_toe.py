from state import get_all_states
from player import RLPlayer, HumanPlayer
from judge import Judge

# Get all possible board configurations
all_states = get_all_states(rows=3, columns=3)

# region Functions

def train(epochs: int, print_every_n: int = 500):
    # region Summary
    """
    Train 2 RL players
    :param epochs: number of epochs for training
    :param print_every_n: number of epochs to print the intermediate win rate
    """
    # endregion Summary

    # region Body

    # Create 2 RL players with ε = 0.01 exploring probability
    player1 = RLPlayer(all_states, epsilon = 0.01)
    player2 = RLPlayer(all_states, epsilon = 0.01)


    # Create a judge to organize the game
    judge = Judge(player1, player2)


    # Set the initial win rate of both players to 0
    player1_win = 0.0
    player2_win = 0.0


    # For every epoch
    for i in range(1, epochs + 1):
        # get the winner
        winner = judge.play(all_states)
        # check which player is the winner
        if winner == 1:
            player1_win += 1
        if winner == -1:
            player2_win += 1

        # print the intermediate win rates, if needed
        if i % print_every_n == 0:
            total_games = player1_win + player2_win

            if total_games > 0:
                p1_rate = (player1_win/total_games)*100
                p2_rate = (player2_win / total_games) * 100
            else:
                p1_rate = p2_rate = 0
            print(f"Game #{i}")
            print(f"Player 1: {p1_rate:.2f}%")
            print(f"Player 2: {p2_rate:.2f}%")

        # update value estimates of both players
        player1.update_state_value_estimates()
        player2.update_state_value_estimates()

        # reset the judge => players
        judge.reset()


    # Save the players' policies
    player1.save_policy("player1_policy")
    player2.save_policy("player2_policy")


    # endregion Body


def compete(turns):
    # region Summary
    """
    Compete trained RL players
    :param turns: number of turns for competition
    """
    # endregion Summary

    # region Body

    # Create 2 RL players with ε = 0 exploring probability (i.e. greedy)
    player1 = RLPlayer(all_states, epsilon = 0)
    player2 = RLPlayer(all_states, epsilon = 0)


    # Create a judge to organize the game
    judge = Judge(player1, player2)


    # Load the players' policies
    player1.load_policy("player1_policy")
    player2.load_policy("player2_policy")

    # Set the initial win rate of both players to 0
    player1_win = 0.0
    player2_win = 0.0


    # For every turn
    for i in range(turns):
        # get the winner
        winner = judge.play(all_states)

        # check which player is the winner
        if winner == 1:
            player1_win += 1
        if winner == -1:
            player2_win ++ 1


        # reset the judge => players
        judge.reset()



    # endregion Body


def play():
    # region Summary
    """
    Play against RL player. The game is a 0-sum game. If both players are playing with an optimal strategy, every game will end in a tie.
    So we test whether the RL can guarantee at least a tie if it plays 2nd.
    """
    # endregion Summary

    # region Body

    while True:
        # Create a human player
        human = HumanPlayer()


        # Create RL player with ε = 0 exploring probability (i.e. greedy)
        rl_player = RLPlayer(all_states, epsilon = 0)


        # Create a judge to organize the game
        judge = Judge(human, rl_player)


        # Load the RL player's policy
        rl_player.load_policy("player2_policy")


        # Get the winner
        winner = judge.play(all_states)


        # Check which player is the winner
        if winner == 1:
            print("You won!")
        if winner == -1:
            print("AI won!")
        else:
            print("Its a draw!")

    # endregion Body

# endregion Functions


if __name__ == '__main__':
    train(epochs=int(1e5))
    compete(turns=int(1e3))
    play()
