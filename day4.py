def parse_input():
    lines = []
    with open("inputs/day4.txt", "r") as fin:
        for line in fin:
            winners, numbers = line.split(":")[1].split("|")
            lines.append(
                (
                    set(
                        (
                            int(winners[i : i + 3])
                            for i in range(0, len(winners.lstrip()), 3)
                        )
                    ),
                    set(
                        (
                            int(numbers[i : i + 3])
                            for i in range(0, len(numbers.lstrip()), 3)
                        )
                    ),
                )
            )

    return lines


def problem1():
    cards = parse_input()
    return sum(map(lambda x: int(2 ** (len(x[0].intersection(x[1])) - 1)), cards))


def problem2():
    cards = parse_input()
    n_cards = [1] * len(cards)
    for i in range(len(n_cards)):
        curr_wins, curr_nums = cards[i]
        n_wins = len(curr_wins.intersection(curr_nums))
        for j in range(n_wins):
            n_cards[i + 1 + j] += n_cards[i]

    return sum(n_cards)


if __name__ == "__main__":
    print(problem1())
    print(problem2())
