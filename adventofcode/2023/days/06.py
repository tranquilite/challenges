from aoc_utils import test_aoc

DAY = '06'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list) -> int:
    """Naive solution. TODO: solve the quadratic in a sane way."""
    times = [int(e) for e in lines[0].split(':')[1].split()]
    distances = [int(e) for e in lines[1].split(':')[1].split()]
    combinations = []
    for time, distance in zip(times, distances):
        candidate = [x for x in range(time+1) if (x * (time-x)) > distance]
        combinations.append(len(candidate))

    margin_of_error = 1
    for combination in combinations:
        margin_of_error *= combination

    return margin_of_error


@test_aoc(DAY, 'part2', timer=True)
def part2(lines: list) -> int:
    """Dag 6 - Part 2. Rewritten to solve algebraiciacaclacacialy"""
    time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))

    r1 = ((time) + (time**2 - 4*distance)**0.5) // 2
    r2 = ((time) - (time**2 - 4*distance)**0.5) // 2

    return int(r1 - r2)


if __name__ == '__main__':
    source = load_input('inputs/day6.txt')

    print(
        part1(source),
        part2(source)
    )
