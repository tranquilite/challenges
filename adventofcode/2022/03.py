# --- Day 3: Rucksack Reorganization ---
PRIORITIES = [*'abcdefghijklmnopqrstuvwxyz']
PRIORITIES.extend([e.upper() for e in PRIORITIES])


def day3_part1(backpacks: list) -> int:
    score = 0
    for backpack in backpacks:
        size, found = len(backpack) // 2, []
        comp1, comp2 = backpack[:size], backpack[size:]  # compartments

        for i in range(len(comp1)):
            if comp1[i] in comp2 \
              and not comp1[i] in found \
              and comp1[i] in PRIORITIES:
                score += PRIORITIES.index(comp1[i]) + 1
                found.append(comp1[i])

    return(score)


def day3_part2(backpacks: list) -> int:
    score = 0

    for i in range(0, len(backpacks), 3):
        found = []
        elf_group = backpacks[i:i+3]

        for e in elf_group[0]:
            if e not in PRIORITIES:
                found.append(e)

            if e in elf_group[1] and e in elf_group[2] and e not in found:
                score += PRIORITIES.index(e) + 1
                found.append(e)

    return score


if __name__ == '__main__':
    backpack = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

    backpack = backpack.splitlines()
    print(day3_part1(backpack))
    print(day3_part2(backpack))

    with open('inputs/day3.txt', mode='r') as fh:
        backpacks = fh.readlines()
        print(day3_part1(backpacks))
        print(day3_part2(backpacks))
