from helper import fprint, lp


@fprint
def part1() -> int:
    with open('inputs/04_t') as fhandle:
        # First line is the draw series
        number_draw = [int(draw) for draw in fhandle.readline().rstrip().split(',')]
        lineset = fhandle.readlines()
        bingomatrix, submatrix, rot_bingomatrix, steps = [], [], [], {}

        for line in lineset:
            if line != '\n':
                submatrix.append([int(e) for e in line.rstrip().split()])
            if len(submatrix) == 5:
                bingomatrix.append(submatrix)
                submatrix = []

    lp(bingomatrix)


if __name__ == '__main__':
    part1()
