from helper import fprint, lp


@fprint
def part1() -> int:
    with open('inputs/03input') as fhandle:
        report = fhandle.readlines()

    matrix = [[line[1] for line in enumerate(e.rstrip())] for e in report]
    L_gamma = [[matrix[row][column] for row in range(len(matrix))]
               for column in range(len(matrix[0]))]

    gamma = ['1' if e.count('1') > e.count('0') else '0' for e in L_gamma]
    epsilon = ['1' if e.count('1') < e.count('0') else '0' for e in L_gamma]

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


@fprint
def part2() -> int:
    """...jeg ble så utrolig lei av denne.."""
    with open('inputs/03input') as fhandle:
        report = fhandle.readlines()
    matrix = [[line  for line in e.strip()] for e in report]

    oxygen = list(matrix)
    for col in range(len(matrix[0])):
        track, top = [0, 0], '0'
        for row in range(len(oxygen)):
            if oxygen[row] is not None :
                if oxygen[row][col] == '0':
                    track[0] += 1
                else:
                    track[1] += 1
        if track[1] >= track[0]:
            top = '1'
 
        for row in range(len(oxygen)):
            if oxygen[row]is not None:
                if oxygen[row][col] != top:
                    oxygen[row] = None

        oxygen = list(filter(None, oxygen))

        if len(oxygen) == 1:
            break

    scrubber = list(matrix)
    for col in range(len(matrix[0])):
        track, top = [0, 0], '0'
        for row in range(len(scrubber)):
            if scrubber[row] is not None :
                if scrubber[row][col] == '0':
                    track[0] += 1
                else:
                    track[1] += 1
        if track[1] < track[0]:
            top = '1'
 
        for row in range(len(scrubber)):
            if scrubber[row]is not None:
                if scrubber[row][col] != top:
                    scrubber[row] = None

        scrubber = list(filter(None, scrubber))

        if len(scrubber) == 1:
            break


    return int(''.join(oxygen[0]), 2) * int(''.join(scrubber[0]), 2)



if __name__ == '__main__':
    part1()
    part2()
