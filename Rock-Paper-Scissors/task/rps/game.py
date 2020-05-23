# Write your code here
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def get_winning_play(play: str):
    if play == ROCK:
        return PAPER
    elif play == PAPER:
        return SCISSORS
    else:
        return ROCK


user_play = input()
winning_play = get_winning_play(user_play)
print(f"Sorry, but computer chose {winning_play}")
