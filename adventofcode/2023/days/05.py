from aoc_utils import test_aoc

DAY = '05'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def helper_mapping_lookup(seed: int, raw_map_lines: list) -> int:
    """Naive solution; walk through everything for input seed."""
    location = seed
    for _, mappings in raw_map_lines:  # [map, [range]]
        idx = 0
        for mapping in mappings:  # nuance. destination-source-length
            if location in range(mapping[1], mapping[1] + mapping[2]):
                idx = location - mapping[1]
                location = mapping[0] + idx
                break
    return location


@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list) -> int:
    seeds = [int(e) for e in lines[0].split(':')[1].split()]
    lines = [line for line in lines[1:] if line]
    raw_map_lines = []

    for line in lines:
        if not line.split()[1].isnumeric():
            raw_map_lines.append([line.replace('map:', '').strip(), []])
        else:
            raw_map_lines[-1][1].append([int(e) for e in line.strip().split()])

    destinations = []
    for seed in seeds:
        destinations.append(helper_mapping_lookup(seed, raw_map_lines))

    destinations.sort()

    return destinations[0]


@test_aoc(DAY, 'part2', timer=True)
def part2(lines: list) -> int:
    seed_line = [int(e) for e in lines[0].split(':')[1].split()]
    lines = [line for line in lines[1:] if line]
    raw_map_lines = []

    for line in lines:
        if not line.split()[1].isnumeric():
            raw_map_lines.append([line.replace('map:', '').strip(), []])
        else:
            raw_map_lines[-1][1].append([int(e) for e in line.strip().split()])

    seed_pairs = [(seed_line[e], seed_line[e+1]) for e in range(0, len(seed_line), 2)]
    dest = 457_535_844  # arbitrary big number(tm) - bad approach

    for pair in seed_pairs:
        print(f'Processing {pair}')
        for seed in range(pair[0], pair[0]+pair[1]):
            dest = (a if (a := helper_mapping_lookup(seed, raw_map_lines)) < dest else dest)

    return dest


def helper_part2_2(map_line):
    ...


@test_aoc(DAY, 'part2', timer=True)
def part2_2(lines: list) -> int:
    seed_line = [int(e) for e in lines[0].split(':')[1].split()]
    lines = [line for line in lines[1:] if line]
    raw_map_lines = []

    for line in lines:
        if not line.split()[1].isnumeric():
            raw_map_lines.append([line.replace('map:', '').strip(), []])
        else:
            raw_map_lines[-1][1].append([int(e) for e in line.strip().split()])

    for map_line in raw_map_lines[::-1]:
        mappings = helper_part2_2(map_line)

    seed_pairs = [(seed_line[e], seed_line[e+1]) for e in range(0, len(seed_line), 2)]
    destination = 457_535_844  # arbitrary big number(tm)



    return destination

if __name__ == '__main__':
    source = load_input('inputs/day5.txt')

    print(
        part1(source),
        part2([])

    )
