from aoc_utils import test_aoc
import math

DAY = '08'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def helper_build_adjacency_list(lines: list) -> dict:
    """Builds an adjacency list for a binary tree"""
    adjacency_list = {}
    for line in lines:  # AAA = (BBB, CCC)
        if not line:
            continue
        node, edges = line.split('=')
        edges = tuple(edges.replace(' ', '')[1:-1].split(','))
        adjacency_list[node.strip()] = (edges)
    return adjacency_list


@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list, start='AAA', target='ZZZ') -> int:
    instructions = [int('0') if e == "L" else 1 for e in lines[0]]
    graph = helper_build_adjacency_list(lines[1:])

    pointer, current_node = 0, start
    while current_node != target:
        current_node = \
            graph[current_node][instructions[pointer % (len(instructions))]]
        pointer += 1  # increment pointer

    return pointer


@test_aoc(DAY, 'part2', timer=True)
def part2(lines: list, start_suffix='A', target_suffix='Z') -> int:
    instructions = [int('0') if e == "L" else 1 for e in lines[0]]
    graph = helper_build_adjacency_list(lines[1:])
    starting_nodes = [node for node in graph if node[2] == start_suffix]

    ptr, searching, steps_to_target, ilen = 0, True, [], len(instructions)

    while searching:
        current_node = starting_nodes[ptr]
        nodeptr, next_node = 0, False
        while not next_node:  # ugh.
            current_node = graph[current_node][instructions[nodeptr % ilen]]
            if current_node[2] == target_suffix:
                steps_to_target.append(nodeptr + 1)
                next_node = True
            nodeptr += 1
        ptr += 1
        if len(steps_to_target) == len(starting_nodes):
            searching = False

    return math.lcm(*steps_to_target)  # bare hvis syklisk


if __name__ == '__main__':
    source = load_input(f'inputs/day{DAY}.txt')

    print(
        part1(source),
        part2(source)
    )
