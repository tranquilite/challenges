# --- Day 5: Supply Stacks ---

def day5_prep(crane_setup: list):
    num_cols, stash = 0, []
    instructions = []

    for line in crane_setup:
        if 'move' in line:  # convert instructions from str to tuple
            line = line.replace('move', '').replace('from', '|') \
                .replace('to', '|').replace(' ', '')
            line = [int(e) for e in line.split('|')]
            # move 18 from 3 to 8
            instructions.append((line[0], line[1], line[2]))
        else:
            if '1' in line:  # note max num of stacks
                num_cols = int([e for e in line if e.isnumeric()][-1])
            else:
                stash.append(line)

    cols = {key: [] for key in range(num_cols)}
    rows = []

    for row_idx in range(0, len(stash)):
        line = stash[row_idx].replace('] ', ']') \
                .replace('   ', '[*]') \
                .replace(' ', '')  # filler
        _ = []
        for idx in range(0, len(line)):
            if line[idx] == '[':
                _.append(line[idx:idx+3])

        if _:
            rows.append(_)

    for col_idx in range(num_cols):
        for row in rows:
            if row[0] != '[*]':
                cols[col_idx].append(row.pop(0))
            else:
                row.pop(0)

    for e in cols:  # reverse order
        cols[e] = cols[e][::-1]

    for e in cols:
        print(e, ''.join(cols[e]))

    return cols, instructions


def day5_part1(stacks: dict, instructions: list) -> str:
    '''
    After the rearrangement procedure completes,
    what crate ends up on top of each stack?
    '''
    top_crate = ''

    # move X from Y to Z
    for order in instructions:
        moves, source, target = order[0], order[1]-1, order[2]-1
        for action in range(moves):  # repeat action (moves) times
            try:
                # appends to target, the element popped from source
                stacks[target].append(stacks[source].pop())
            except IndexError:
                print('p1 failed on', action, moves, source, target)

    for column in stacks:
        _ = stacks[column][-1].replace('[', '').replace(']', '')
        top_crate = top_crate + _

    return top_crate


def day5_part2(stacks: dict, instructions: list) -> int:
    '''
    After the rearrangement procedure completes,
    what crate ends up on top of each stack?
    '''
    top_crate = ''
    # move X from Y to Z
    for order in instructions:
        moves, source, target = order[0], order[1]-1, order[2]-1
        col = stacks[source]
        get, left = col[-moves:], col[0:-moves]
        stacks[source] = left
        stacks[target].extend(get)

    for column in stacks:
        _ = stacks[column][-1].replace('[', '').replace(']', '')
        top_crate = top_crate + _

    return top_crate


if __name__ == '__main__':
    crane_setup = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

    crane_setup = crane_setup.splitlines()

    print(day5_part1(*day5_prep(crane_setup)))
    print(day5_part2(*day5_prep(crane_setup)))

    print()

    with open('inputs/day5.txt', mode='r') as fh:
        setup = fh.readlines()

    print(day5_part1(*day5_prep(setup)))
    print(day5_part2(*day5_prep(setup)))
