# --- Day 2: Rock Paper Scissors ---
# A Rock, B Paper, C Scissors | X Rock, Y Paper, Z Scissors
WEIGHTS = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
WINS = {'A': 'Z', 'B': 'X', 'C': 'Y', 'X': 'C', 'Y': 'A', 'Z': 'B'}
PART2 = {key: key for key in [*'ABCXYZ']}


def day2_part1(game: list) -> int:

    score = 0

    for round in game:
        moves = round.split()

        if moves[0] == WINS[moves[1]]:
            score += 6 + WEIGHTS[moves[1]]
        elif moves[1] == WINS[moves[0]]:
            score += 0 + WEIGHTS[moves[1]]
        else:
            score += 3 + WEIGHTS[moves[1]]
    return score


def day2_part2(game: list) -> int:
    # X, lose, Y, draw, Z win
    score = 0

    for round in game:
        moves = round.split()

        if moves[1] == 'Y':  # draw
            score += 3 + WEIGHTS[moves[0]]
        elif moves[1] == 'X':  # lose
            score += 0 + WEIGHTS[WINS[moves[0]]]
        else:  # win
            score += 6 + WEIGHTS[WINS[WINS[moves[0]]]]

    return score


if __name__ == '__main__':
    elf_crib = '''A Y
B X
C Z'''

    elf_guide_split = elf_crib.splitlines()
    print(day2_part1(elf_guide_split) == 15)
    print(day2_part2(elf_guide_split) == 12)

    with open('inputs/day2.txt', mode='r') as fh:
        elf_crib = fh.readlines()

        print(day2_part1(elf_crib))
        print(day2_part2(elf_crib))
