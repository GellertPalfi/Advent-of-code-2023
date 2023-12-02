import math


def read_file(path):
    all_games = []
    with open(path, "r") as file:
        for line in file:
            id_str, games_str = line.split(":")
            games_list = games_str.strip().split(";")
            game_dict = {"id": id_str.strip()}
            game_dict.update(
                {str(index): game.strip() for index, game in enumerate(games_list)}
            )
            all_games.append(game_dict)
    return all_games


def solution_1(games):
    total_sum = 0
    for game in games:
        id_ = int(game["id"].split(" ")[1])
        if all(
            check_color_count(color, int(number))
            for key, value in game.items()
            if key != "id"
            for number, color in (pair.strip().split(" ") for pair in value.split(","))
        ):
            total_sum += id_

    return total_sum


def solution_2(games):
    total_power = 0
    for game in games:
        min_dict = {"red": 0, "green": 0, "blue": 0}
        for value in list(game.values())[1:]:
            values = value.split(",")
            for one_game in values:
                number, color = one_game.strip().split(" ")
                min_dict[color] = max(min_dict[color], int(number))

        total_power += math.prod(dict.values(min_dict))
    return total_power


def check_color_count(color, count_):
    if color == "red" and count_ > 12:
        return False
    if color == "green" and count_ > 13:
        return False
    if color == "blue" and count_ > 14:
        return False
    return True


if __name__ == "__main__":
    path = "inputs/day2_input.txt"
    games = read_file(path)
    sum = solution_1(games)
    print(sum)
    power = solution_2(games)
    print(power)
