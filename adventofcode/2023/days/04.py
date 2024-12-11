from aoc_utils import test_aoc


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def helper_splitline(line: str) -> tuple:
    card_num, _ = line.split(':')
    card_num = int(card_num.split()[1])
    winning_num, my_num = _.strip().split('|')
    winning_num = winning_num.strip().split()
    my_num = my_num.strip().split()

    return (card_num, winning_num, my_num)


@test_aoc('04', 'part1', timer=True)
def part1(lines: list) -> int:
    score = 0
    for line in lines:
        _ = helper_splitline(line)
        winning_num, my_num = _[1], _[2]
        isct = list(set(winning_num) & set(my_num))

        score += 2**(len(isct)-1) if len(isct) >= 1 else 0
    return score


@test_aoc('04', 'part2', timer=True)
def part2(lines: list) -> int:
    wins = []
    card_counts = [1 for card in range(len(lines))]

    for lno, line in enumerate(lines):
        card_num, winning_num, my_num = helper_splitline(line)
        wins.append(len(list(set(winning_num) & set(my_num))))

    for idx in range(len(card_counts)):
        if wins[idx] > 0:
            for e in range(card_counts[idx]):
                for i in range(idx+1, idx+wins[idx]+1):
                    card_counts[i] += 1

    return sum(card_counts)


if __name__ == '__main__':
    source = load_input('inputs/day4.txt')

    print(
        part1(source),
        part2(source)
    )
