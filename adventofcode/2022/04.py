# --- Day 4: Camp Cleanup ---

def day4_part1(section_assigments: list) -> int:
    '''In how many assignment pairs does one range fully contain the other?'''
    score = 0

    for pair in section_assigments:
        pair = pair.replace(',', '-').split('-')
        e1, e2 = [int(e) for e in pair[:2]], [int(e) for e in pair[2:]]

        if e1[0] <= e2[0] and e1[1] >= e2[1] or \
                e2[0] <= e1[0] and e2[1] >= e1[1]:
            score += 1

    return score


def day4_part2(section_assigments: list) -> int:
    '''In how many assignment pairs do the ranges overlap?'''
    score = 0

    for pair in section_assigments:
        pair = pair.replace(',', '-').split('-')
        e1, e2 = [int(e) for e in pair[:2]], [int(e) for e in pair[2:]]

        e1 = [e for e in range(e1[0], e1[1]+1)]
        e2 = [e for e in range(e2[0], e2[1]+1)]

        for e in e1:
            if e in e2:
                score += 1
                break  # only counting pairs that have _at least one overlap_

    return score


if __name__ == '__main__':
    elf_assign = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

    elf_assign = elf_assign.splitlines()

    print(day4_part1(elf_assign))
    print(day4_part2(elf_assign))

    with open('inputs/day4.txt', mode='r') as fh:
        elf_assign = fh.readlines()

        print(day4_part1(elf_assign))
        print(day4_part2(elf_assign))
