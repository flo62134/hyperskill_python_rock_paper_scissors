# Write your code here
import random
import os

USER_GREETING = 'Hello, {0}'

SCORE_FILE = 'rating.txt'

INVALID_INPUT = 'Invalid input'

EXIT = '!exit'
RATING = '!rating'
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
PLAYS = [ROCK, PAPER, SCISSORS]
OPTIONS = [ROCK, PAPER, SCISSORS, EXIT, RATING]

ASK_USERNAME = 'Enter your name:'
LOSE = 'Sorry, but computer chose {0}'
LOSE_SCORE = 0
DRAW = 'There is a draw ({0})'
DRAW_SCORE = 50
WIN = 'Well done. Computer chose {0} and failed'
WIN_SCORE = 100
YOUR_RATING = "Your rating: {0}"
END = 'Bye!'


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

    return round_state


def is_valid_word(word: str):
    return word in OPTIONS


def ask_username():
    return input(ASK_USERNAME)


def greet_player(username: str):
    print(USER_GREETING.format(username))


def get_user_score(username: str):
    if os.path.exists(SCORE_FILE):
        file = open(SCORE_FILE, 'rt')
        score = 0

        for line in file:
            line_username = line.split()[0]
            line_score = line.split()[1]
            if line_username == username:
                score = line_score

        return score
    else:
        return 0


def display_score(score: int):
    score = str(score)
    print(YOUR_RATING.format(score))


def apply_round_score(current_score: int, round_state: str):
    if round_state == WIN:
        round_score = 100
    elif round_state == DRAW:
        round_score = 50
    else:
        round_score = 0

    return current_score + round_score


user_play = ''
username = ask_username()
greet_player(username)
score = get_user_score(username)

while user_play != EXIT:
    user_play = input()
    is_valid = is_valid_word(user_play)
    if not is_valid:
        print(INVALID_INPUT)
        continue

    if user_play == RATING:
        display_score(score)
        continue

    if user_play in PLAYS:
        round_state = play_round(user_play)
        score = apply_round_score(score, round_state)

print(END)
