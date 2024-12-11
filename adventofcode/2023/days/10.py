from aoc_utils import test_aoc

DAY = '10'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def build_path(lines) -> list:
    lin_graph = []
    sym_valid_nodes = [*'|-LJ7F-S']
    for y, line in enumerate(lines):
        if 'S' in line:
            lin_graph.append((line.index('S'), y))

    current_coord, scanning = lin_graph[0], True
    while scanning:
        x, y = current_coord[0], current_coord[1]

        rdlu = lines[x+1, lines[]]

        if current_coord == lin_graph[0]:
            scanning = False

    return lin_graph

@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list) -> int:
    graph = build_path(lines)

    print(graph)
    return 12


@test_aoc(DAY, 'part2', timer=True)
def part2(lines: list) -> int:
    ...


if __name__ == '__main__':
    source = load_input(f'inputs/day{DAY}.txt')

    print(
        part1(source),
        #part2(source)
    )
