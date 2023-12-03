def parse_input():
    games = []
    with open("inputs/day2.txt", "r") as fin:
        for game in fin:
            subsets = game.split(":")[1].strip().split(";")

            games.append(
                [
                    list(
                        map(
                            lambda x: (int(x.strip().split()[0]), x.strip().split()[1]),
                            subset.split(","),
                        )
                    )
                    for subset in subsets
                ]
            )
        return games


def problem1():
    games = parse_input()
    acc = 0
    limits = {"red": 12, "green": 13, "blue": 14}
    for i, game in enumerate(games, start=1):
        plays = [p for g in game for p in g]
        acc += (
            i
            if all(map(lambda x: x[1] in limits.keys() and x[0] <= limits[x[1]], plays))
            else 0
        )

    return acc


def problem2():
    games = parse_input()
    acc = 0
    for game in games:
        curr_game = 1
        for color in ("red", "green", "blue"):
            plays = [p for g in game for p in g]
            color_extract = filter(lambda x: x[1] == color, plays)
            curr_game *= sorted(color_extract, key=lambda x: x[0])[-1][0]

        acc += curr_game

    return acc


if __name__ == "__main__":
    print(problem1())
    print(problem2())
