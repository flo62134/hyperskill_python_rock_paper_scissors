# Write your code here
import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
PLAYS = [ROCK, PAPER, SCISSORS]

LOSE = 'Sorry, but computer chose {0}'
DRAW = 'There is a draw ({0})'
WIN = 'Well done. Computer chose {0} and failed'


def get_winning_play(play: str):
    if play == ROCK:
        return PAPER
    elif play == PAPER:
        return SCISSORS
    else:
        return ROCK


def get_round_state(user_play: str, computer_play: str):
    winning_play = get_winning_play(user_play)

    if user_play == computer_play:
        return DRAW

    return LOSE if computer_play == winning_play else WIN


def format_round_state(state: str, computer_play: str):
    return state.format(computer_play)


user_play = input()
computer_play = random.choice(PLAYS)
round_state = get_round_state(user_play, computer_play)
print(format_round_state(round_state, computer_play))
