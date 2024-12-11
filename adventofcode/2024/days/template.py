from typing import List
from aoc_utils import test_aoc

DAY = '0'
RUN_TESTS = True

# 


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


@test_aoc(DAY, 'part1', timer=True, run_test=RUN_TESTS)
def part1(lines: List[str]) -> int:
    ...


@test_aoc(DAY, 'part2', timer=True, run_test=RUN_TESTS)
def part2(lines: List[str]) -> int:
    ...


if __name__ == '__main__':
    source = load_input(f'inputs/{DAY}.txt')

    print(
        part1(source),
        part2(source)
    )
