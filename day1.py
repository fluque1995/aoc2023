def parse_input():
    with open("inputs/day1.txt", "r") as fin:
        lines = [line.rstrip() for line in fin]
    return lines


def problem1():
    lines = parse_input()
    digits = list(map(str, range(10)))
    numbers = list(map(lambda y: list(filter(lambda x: x in digits, y)), lines))
    return sum(map(lambda x: 10 * int(x[0]) + int(x[-1]), numbers))


def problem2():
    def names_to_digits(code):
        substitutions = [
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
        ]
        completion = ""
        for i in range(len(code)):
            for orig, dest in substitutions:
                if code[i : i + len(orig)] == orig:
                    completion = completion + dest
            else:
                completion = completion + code[i]

        return completion

    lines = parse_input()
    lines = list(map(names_to_digits, lines))
    digits = list(map(str, range(10)))
    numbers = list(map(lambda y: list(filter(lambda x: x in digits, y)), lines))
    return sum(map(lambda x: 10 * int(x[0]) + int(x[-1]), numbers))


if __name__ == "__main__":
    print(problem1())
    print(problem2())
