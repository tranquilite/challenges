from helper import fprint

keywd = ['UP', 'DOWN', 'FORWARD']


@fprint
def part1() -> int:
    directions, hor, vert = [], 0, 0

    with open('inputs/02input') as fhandle:
        for line in fhandle.readlines():
            grief = list(map(lambda x: int(x) if x.isdigit() else x[0].upper(),
                             line.rstrip().split()))
            directions.append((grief[0], grief[1]))

    hor += sum(map(lambda x: int(x[1]) if x[0] == 'F' else False, directions))
    vert += sum(map(lambda x: int(x[1]) if x[0] == 'D' else False, directions))
    vert -= sum(map(lambda x: int(x[1]) if x[0] == 'U' else False, directions))

    return hor*vert


@fprint
def part2() -> int:
    directions, hor, vert, aim = [], 0, 0, 0

    with open('inputs/02input') as fhandle:
        for line in fhandle.readlines():
            grief = list(map(lambda x: int(x) if x.isdigit() else x[0].upper(),
                             line.rstrip().split()))
            directions.append((grief[0], grief[1]))

    for action in directions:
        if action[0] == 'D':
            aim += action[1]
        if action[0] == 'U':
            aim -= action[1]
        if action[0] == 'F':
            hor += action[1]
            vert += (aim*action[1])

    return hor*vert


if __name__ == '__main__':
    part1()
    part2()
