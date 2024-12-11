from aoc_utils import test_aoc

DAY = '0'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list) -> int:
    ...


@test_aoc(DAY, 'part2', timer=True)
def part2(lines: list) -> int:
    ...


if __name__ == '__main__':
    source = load_input(f'inputs/day{DAY}.txt')

    print(
        part1(source),
        part2(source)
    )
