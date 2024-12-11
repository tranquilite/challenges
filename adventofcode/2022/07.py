# --- Day 7: No Space Left On Device ---

def day7_part1(terminal_output: list) -> int:
    '''
    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    '''

    total_size = 0
    path, cwd = [], {}
    tree = {}

    for line in terminal_output:
        line = line.split()

        if line[0] == '$':  # line is input
            if line[1] == 'cd':
                print(f'In {path}, entering {line[2]}')
                if line[2] == '..':
                    path.pop()  # walk back
                else:
                    path.append(line[2])  # add to path
                tree[path[-1]] = dict(cwd)
                cwd = {}  # reset :)
        elif line[0].isnumeric():
            print(f'\t{line[1]}\t{line[0]}')
            cwd[line[1]] = int(line[0])
        elif line[0] == 'dir':
            print(f'\t{line[1]}\t{line[0]}')
            cwd[line[1]] = {}

    for e in tree:
        print(e, tree[e])
        
    '''
    tree = { '/':
        {
            'b.txt': 14848514,
            'c.dat': 8504156,
            'a': {
                'f': 29116,
                'g': 2557,
                'h.lst': 62596
            } 
            'd': 'dir'}
    }
    '''

    return total_size


def day7_part2() -> int:
    return False


if __name__ == '__main__':
    terminal_output = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

    terminal_output = terminal_output.splitlines()

    print(day7_part1(terminal_output))


    with open('inputs/day7.txt', mode='r') as fh:
        setup = fh.readlines()
