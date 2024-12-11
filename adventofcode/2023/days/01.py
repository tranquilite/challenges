from examples.day1 import part2test as p2t


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def part1(lines: list) -> int:
    calibration_values = []

    # TODO: Refactor this to like .. 4 lines
    for line in lines:
        val = [None, None]
        for char in line:
            if char.isnumeric():
                val[0] = char
                break
        for char in line[::-1]:
            if char.isnumeric():
                val[1] = char
                break

        calibration_values.append(int(''.join(val)))

    return sum(calibration_values)


def search_substrings(string, substring, *, offset=0, indices=[]):
    if substring in string:
        idx = string.find(substring)
        indices.append((idx + offset, substring))
        return search_substrings(
            string[idx + len(substring)-2:], substring,
            offset=offset + idx + len(substring) - 2, indices=indices)
    else:
        return indices


def part2(lines: list) -> int:
    valid_terms = ['one', 'two', 'three', 'four',
                   'five', 'six', 'seven', 'eight', 'nine']
    calibration_values = []

    for line in lines:
        indices, substrings = [], []

        for term in valid_terms:
            substring_instances = search_substrings(line, term, indices=[])
            if substring_instances:
                for instance in substring_instances:
                    substrings.append(
                        (instance[0], str(valid_terms.index(instance[1])+1)))

        indices.extend(substrings)

        for idx in range(len(line)):
            char = line[idx]
            if char.isnumeric():
                indices.append((idx, char))

        indices.sort(key=lambda x: x[0])
        calibration_values.append(
            int(''.join([indices[0][1], indices[-1][1]])))

    return sum(calibration_values)


if __name__ == '__main__':
    p2t(part2)

    source = load_input('inputs/day1.txt')
    print(f'Got {part1(source)}')
    print(f'Got {part2(source)}')  # 53188 "too low", 53204 "too low"
