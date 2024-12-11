from aoc_utils import test_aoc

DAY = '01'
RUN_TESTS = True

# --- Day 1: Historian Hysteria ---


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


@test_aoc(DAY, 'part1', timer=True, run_test=RUN_TESTS)
def part1(lines: list) -> int:
    team1, team2 = [], []

    for line in lines:
        _ = line.split()
        team1.append(int(_[0]))
        team2.append(int(_[1]))

    return sum(
        map(lambda x: abs(x[0]-x[1]), zip(sorted(team1), sorted(team2)))
    )


@test_aoc(DAY, 'part2', timer=True, run_test=RUN_TESTS)
def part2(lines: list) -> int:
    team1, team2 = [], []

    for line in lines:
        _ = line.split()
        team1.append(int(_[0]))
        team2.append(int(_[1]))

    return sum(
        map(lambda x: x * team2.count(x), team1)
    )


if __name__ == '__main__':
    source = load_input(f'inputs/{DAY}.txt')

    print(
        part1(source),
        part2(source)
    )
