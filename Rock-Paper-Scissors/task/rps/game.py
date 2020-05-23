# Write your code here
import random

INVALID_INPUT = 'Invalid input'

END = 'Bye!'

EXIT = '!exit'

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
PLAYS = [ROCK, PAPER, SCISSORS]

LOSE = 'Sorry, but computer chose {0}'
DRAW = 'There is a draw ({0})'
WIN = 'Well done. Computer chose {0} and failed'


def get_computer_winning_play(user_play: str):
    if user_play == ROCK:
        return PAPER
    elif user_play == PAPER:
        return SCISSORS
    else:
        return ROCK


def get_round_state(user_play: str, computer_play: str):
    winning_play = get_computer_winning_play(user_play)

    if user_play == computer_play:
        return DRAW

    return LOSE if computer_play == winning_play else WIN


def format_round_state(state: str, computer_play: str):
    return state.format(computer_play)


def play_round(user_play: str):
    computer_play = random.choice(PLAYS)
    round_state = get_round_state(user_play, computer_play)
    print(format_round_state(round_state, computer_play))


def is_valid_play(play: str):
    return play in PLAYS


user_play = ''
while user_play != EXIT:
    user_play = input()
    is_valid = is_valid_play(user_play)
    if not is_valid:
        print(INVALID_INPUT)
        continue

    play_round(user_play)

print(END)
