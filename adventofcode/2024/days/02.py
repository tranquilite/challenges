from typing import List
from aoc_utils import test_aoc

DAY = '02'
RUN_TESTS = False

# --- Day 2: Red-Nosed Reports ---


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def strictly_increasing(lst: List[int]):
    return all(0 < (lst[i] - lst[i+1]) <= 3 for i in range(len(lst)-1))

def strictly_decreasing(lst: List[int]):
    return all(0 > (lst[i] - lst[i+1]) >= -3 for i in range(len(lst)-1))

@test_aoc(DAY, 'part1', run_test=RUN_TESTS)
def part1(lines: list) -> int:
    safe_reports: int = 0

    for report in lines:
        readings: List[int] = [int(e) for e in report.split()]

        if strictly_decreasing(readings) or strictly_increasing(readings):
            safe_reports += 1

    return safe_reports


@test_aoc(DAY, 'part2', run_test=RUN_TESTS)
def part2(lines: list) -> int:
    safe_reports: int = 0

    sign = lambda x: (x > 0) - (x < 0)

    for report in lines:
        lst: List[int] = [int(e) for e in report.split()]
        prev = -9999

        if strictly_decreasing(lst) or strictly_increasing(lst):
                safe_reports += 1
        else:
            print(f'Foo {lst}')
            for idx in range(len(lst) - 1):
                diff = lst[idx] - lst[idx+1]
                prev = diff if prev == -9999 else prev

                if abs(diff) > 3 or diff != 0 and sign(diff) != sign(prev):
                    lst.pop(idx)
                    break
                prev = diff

            if strictly_decreasing(lst) or strictly_increasing(lst):
                    print(f'\tIncrement: {lst}')
                    safe_reports += 1

    return safe_reports
                    


if __name__ == '__main__':
    source = load_input(f'inputs/{DAY}.txt')

    print(
        part1(source),
        part2(source)
    )
