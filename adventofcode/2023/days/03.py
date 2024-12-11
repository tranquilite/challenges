from aoc_utils import test_aoc


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


@test_aoc('03', 'part1')
def part1(lines: list) -> int:

    return 12


def part2(lines: list) -> int:
    ...


if __name__ == '__main__':
    source = load_input('inputs/day3.txt')

    part1(source)


# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# [row-1][col-1] [row-1][col] [row-1][col+1]
# [row][col-1]    [row][col]  [row][col+1]
# [row+1][col-1] [row+1][col] [row+1][col+1]
