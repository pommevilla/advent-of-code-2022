player_values = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

player_throws = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

player_outcomes = {
    'X': "lose",
    'Y': "draw",
    'Z': "win"
}

opponent_throws = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

paper_dict = {
    "rock": "win",
    "paper": "draw",
    "scissors": "lose"
}

rock_dict = {
    "rock": "draw",
    "paper": "lose",
    "scissors": "win"
}

scissors_dict = {
    "rock": "lose",
    "paper": "win",
    "scissors": "draw"
}

game_result_points = {
    "lose": 0,
    "draw": 3,
    "win": 6
}


def get_key_by_value(rps_dict: dict[str, str], outcome: str) -> str:
    if outcome == "win":
        outcome = "lose"
    elif outcome == "lose":
        outcome = "win"
    else:
        outcome = "draw"
    return list(rps_dict.keys())[list(rps_dict.values()).index(outcome)]


def resolve_game_1(player_throw: str, opponent_throw: str) -> int:
    player_throw = player_throws[player_throw]
    opponent_throw = opponent_throws[opponent_throw]
    game_result = ""
    if player_throw == "rock":
        game_result = rock_dict[opponent_throw]
    elif player_throw == "scissors":
        game_result = scissors_dict[opponent_throw]
    else:
        game_result = paper_dict[opponent_throw]

    return game_result_points[game_result] + player_values[player_throw]


def resolve_game_2(player_outcome: str, opponent_throw: str) -> int:
    player_outcome = player_outcomes[player_outcome]
    opponent_throw = opponent_throws[opponent_throw]

    points = game_result_points[player_outcome]

    if opponent_throw == "rock":
        player_throw = get_key_by_value(rock_dict, player_outcome)
    elif opponent_throw == "paper":
        player_throw = get_key_by_value(paper_dict, player_outcome)
    else:
        player_throw = get_key_by_value(scissors_dict, player_outcome)

    points += player_values[player_throw]

    return points


# For testing on the command line
# def main():
#     import argparse
#     parser = argparse.ArgumentParser(description="RPS")
#     parser.add_argument('-p', '--player_throw', type=str)
#     parser.add_argument('-o', '--opponent_throw', type=str)

#     args = parser.parse_args()
#     player_throw = player_throws[args.player_throw]
#     opponent_throw = opponent_throws[args.opponent_throw]

#     points = resolve_game(player_throw=player_throw,
#                           opponent_throw=opponent_throw)
#     print(f'{player_throw=}\t{opponent_throw=}')
#     print(f'{points=}')


def main():
    with open("input.txt") as fin:
        total_score = 0
        line_counter = 0
        for line in fin:
            opponent_throw, player_throw = line.split()
            # points = resolve_game_1(player_outcome=player_throw,
            # opponent_throw=opponent_throw)
            points = resolve_game_2(player_outcome=player_throw,
                                    opponent_throw=opponent_throw)
            total_score += points
            line_counter += 1

    print(f'Total score following strategy: {total_score}')


if __name__ == '__main__':
    main()
