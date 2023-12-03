def parse_input():
    with open("inputs/day3.txt", "r") as fin:
        return [l.strip() for l in fin]


def problem1():
    lines = parse_input()
    symbols = set(
        [
            elem
            for line in map(
                lambda x: list(filter(lambda y: y != "." and not y.isdigit(), x)), lines
            )
            for elem in line
        ]
    )

    def adjacent_symbol(row, init_col, final_col):
        if row > 0:
            for i in range(max(init_col - 1, 0), min(final_col + 2, len(lines[0]))):
                if lines[row - 1][i] in symbols:
                    return True
        if row < len(lines) - 1:
            for i in range(max(init_col - 1, 0), min(final_col + 2, len(lines[0]))):
                if lines[row + 1][i] in symbols:
                    return True
        if init_col > 0 and lines[row][init_col - 1] in symbols:
            return True
        if final_col < len(lines[0]) - 1 and lines[row][final_col + 1] in symbols:
            return True

        return False

    acc = 0
    for j, line in enumerate(lines):
        in_number = False
        for i in range(len(line)):
            if line[i].isdigit() and not in_number:
                in_number = True
                init_pos = i
            elif not line[i].isdigit() and in_number:
                in_number = False
                if adjacent_symbol(j, init_pos, i - 1):
                    acc += int(line[init_pos:i])
            elif i == len(line) - 1 and in_number:
                in_number = False
                if adjacent_symbol(j, init_pos, i - 1):
                    acc += int(line[init_pos : i + 1])

    return acc


def problem2():
    lines = parse_input()

    def surrounding_numbers(row, col):
        nums = []

        def half_line_digits(r, c):
            n = []
            if c > 0 and lines[r][c - 1].isdigit():
                j = c - 1
                while j >= 0 and lines[r][j].isdigit():
                    j -= 1
                n.append(int(lines[r][j + 1 : c]))
            if c < len(lines[r]) - 1 and lines[r][c + 1].isdigit():
                j = c + 1
                while j < len(lines[0]) and lines[r][j].isdigit():
                    j += 1
                n.append(int(lines[r][c + 1 : j]))
            return n

        def full_line_digit(r, c):
            j = k = c
            while j >= 0 and lines[r][j].isdigit():
                j -= 1
            while k <= len(lines[0]) and lines[r][k].isdigit():
                k += 1
            return [int(lines[r][j + 1 : k])]

        nums.extend(half_line_digits(row, col))

        if row > 0:
            if lines[row - 1][col].isdigit():
                nums.extend(full_line_digit(row - 1, col))
            else:
                nums.extend(half_line_digits(row - 1, col))

        if row < len(lines) - 1:
            if lines[row + 1][col].isdigit():
                nums.extend(full_line_digit(row + 1, col))
            else:
                nums.extend(half_line_digits(row + 1, col))

        return nums

    acc = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "*":
                numbers = surrounding_numbers(i, j)
                if len(numbers) == 2:
                    acc += numbers[0] * numbers[1]

    return acc


if __name__ == "__main__":
    print(problem1())
    print(problem2())
