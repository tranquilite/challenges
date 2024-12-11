from helper import fprint


@fprint
def day01_p1() -> int:
    counter, prev = 0, 191  # first case
    with open('inputs/01input') as fhandle:
        measurements = fhandle.readlines()
        for depth in measurements:
            depth = int(depth)
            if depth > prev:
                counter += 1
            prev = depth

    return counter


@fprint
def day01_p2() -> int:
    measuregroups, offset, counter, prev = [], 0, 0, 564

    with open('inputs/01input') as fhandle:
        measurements = fhandle.readlines()
        measurements = list(map(int, measurements))

        for e in range(len(measurements)):
            measuregroups.append(measurements[0+offset] +
                                 measurements[1+offset] +
                                 measurements[2+offset])
            offset += 1
            if (2 + offset) >= len(measurements):
                break

    for depth in measuregroups:
        if depth > prev:
            counter += 1
        prev = depth

    return(counter)


if __name__ == '__main__':
    day01_p1()
    day01_p2()
