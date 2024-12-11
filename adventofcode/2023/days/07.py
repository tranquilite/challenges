from aoc_utils import test_aoc
import io

log = io.StringIO()

DAY = '07'


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def helper_hand_rank(hand: str):
    """This just gets uglier by the minute"""
    state = {key: hand.count(key) for key in [card for card in hand]}
    scores = {(5,): 6, (4, 1): 5, (3, 2): 4, (3, 1, 1): 3,
              (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}
    _ = sorted(list(state.values()), reverse=True)
    print(scores[tuple(_)], file=log, end=' ')
    return scores[tuple(_)]  # type: ignore


def helper_compare_cards(lhs: list, rhs: list) -> tuple:
    """Takes two hands, compares the value of the cards and returns in order"""
    RANK = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for leftcard, rightcard in zip(map(RANK.index, lhs[1]),
                                   map(RANK.index, rhs[1])):
        if leftcard > rightcard:
            return lhs, rhs
        elif leftcard < rightcard:
            return rhs, lhs
        else:  # implicit leftcard == rightcard
            continue
    return lhs, rhs


@test_aoc(DAY, 'part1', timer=True)
def part1(lines: list) -> int:
    hands = []
    for line in lines:
        hand, bet = line.strip().split()
        print(hand, file=log, end=' ')
        hands.append([helper_hand_rank(hand), hand, int(bet)])
        print(int(bet), file=log)
    hands.sort(key=lambda x: x[0], reverse=True)

    for idx in range(len(hands)-1):
        if hands[idx][0] == hands[idx+1][0]:
            hands[idx], hands[idx+1] = helper_compare_cards(
                hands[idx], hands[idx+1])

    wins = [card[2]*(len(hands)+1-e) for e, card in enumerate(hands)]
    print(wins)

    return sum(wins)


@test_aoc(DAY, 'part2', timer=True)  # 248808811
def part2(lines: list) -> int:  # 248308311
    ...                         # 249280060


if __name__ == '__main__':
    try:
        source = load_input('inputs/day7.txt')
    except FileNotFoundError:
        print('Mangler dagens input..')
    else:
        print(
            part1(source)
        )
    finally:
        with open('d7.log', mode='w') as fh:
            fh.write(log.getvalue())
