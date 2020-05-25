# Write your code here
import random
import os
import typing

RULES_SEPARATOR = ','
SCORE_FILE = 'rating.txt'

EXIT = '!exit'
RATING = '!rating'
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
DEFAULT_RULES = [ROCK, PAPER, SCISSORS]
OPTIONS = [EXIT, RATING]

INVALID_INPUT = 'Invalid input'
USER_GREETING = 'Hello, {0}'
ASK_USERNAME = 'Enter your name:'
LOSE = 'Sorry, but computer chose {0}'
LOSE_SCORE = 0
DRAW = 'There is a draw ({0})'
DRAW_SCORE = 50
WIN = 'Well done. Computer chose {0} and failed'
WIN_SCORE = 100
YOUR_RATING = "Your rating: {0}"
END = 'Bye!'


def get_computer_winning_play(user_play: str, rules: typing.List[str]):
    user_play_index = rules.index(user_play)

    rules_copy = rules[:]
    rotating_index = user_play_index + 1
    rotated_rules = rules_copy[rotating_index:] + rules_copy[:rotating_index]

    length = len(rotated_rules)
    return rotated_rules[0:(length // 2)]


def get_round_state(user_play: str, computer_play: str, rules: typing.List[str]):
    winning_plays = get_computer_winning_play(user_play, rules)

    if user_play == computer_play:
        return DRAW

    return LOSE if computer_play in winning_plays else WIN


def format_round_state(state: str, computer_play: str):
    return state.format(computer_play)


def play_round(user_play: str, rules: typing.List[str]):
    computer_play = random.choice(rules)
    round_state = get_round_state(user_play, computer_play, rules)
    print(format_round_state(round_state, computer_play))

    return round_state


def is_valid_word(word: str, rules: typing.List[str]):
    return word in OPTIONS or word in rules


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

        return int(score)
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


def ask_rules():
    rules = input()
    if rules == '':
        return DEFAULT_RULES

    return rules.split(RULES_SEPARATOR)


user_play = ''
username = ask_username()
greet_player(username)
rules = ask_rules()
print('Okay, let\'s start')
score = get_user_score(username)

while user_play != EXIT:
    user_play = input()
    is_valid = is_valid_word(user_play, rules)
    if not is_valid:
        print(INVALID_INPUT)
        continue

    if user_play == RATING:
        display_score(score)
        continue

    if user_play in rules:
        round_state = play_round(user_play, rules)
        score = apply_round_score(score, round_state)

print(END)
