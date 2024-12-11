from aoc_utils import test_aoc

DAY = '09'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def helper_build_history(line: str) -> list:
    history = [[int(e) for e in line.strip().split()]]

    while not all(map(lambda x: x == 0, history[-1])):
        history.append([
            history[-1][e] - history[-1][e-1] for
            e in range(1, len(history[-1]))
        ])

    return history


@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list) -> int:
    running_total = 0

    for line in lines:
        history = helper_build_history(line)

        for idx in range(len(history)-1, 0, -1):
            history[idx-1].append(history[idx-1][-1] + history[idx][-1])

        running_total += history[0][-1]

    return running_total


@test_aoc(DAY, 'part2', timer=True)
def part2(lines: list) -> int:
    running_total = 0

    for line in lines:
        history = helper_build_history(line)

        for idx in range(len(history)-1, 0, -1):
            history[idx-1].insert(0, history[idx-1][0] - history[idx][0])

        running_total += history[0][0]

    return running_total


if __name__ == '__main__':
    source = load_input(f'inputs/day{DAY}.txt')

    print(
        part1(source),
        part2(source)
    )
