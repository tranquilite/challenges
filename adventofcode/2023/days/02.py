from examples.day2 import t_part1, t_part2


def load_input(fname: str) -> list:
    with open(fname, 'r') as fh:
        lines = [e.strip() for e in fh.readlines()]
    return lines


def part1(lines: list, constraint: dict) -> int:
    games = {}
    for line in lines:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game = int(line.replace('Game', '').split(':')[0].strip())
        games[game] = {"red": 0, "green": 0, "blue": 0}

        bundles = line.split(':')[1].strip().split(';')
        for bundle in bundles:
            _items = bundle.split(',')
            for item in _items:
                count, color = int(item.split()[0]), item.split()[1].strip()
                if games[game][color] < count:
                    games[game][color] = count

    poplist = []
    for game in games:
        for key in constraint:
            if games[game][key] > constraint[key]:
                # don't do flow like this :)
                poplist.append(game) if game not in poplist else ...

    for key in poplist:
        games.pop(key)

    return sum(games.keys())


def part2(lines: list):
    games = {}
    for line in lines:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game = int(line.replace('Game', '').split(':')[0].strip())
        games[game] = {"red": 0, "green": 0, "blue": 0}

        bundles = line.split(':')[1].strip().split(';')
        for bundle in bundles:
            _items = bundle.split(',')
            for item in _items:
                count, color = int(item.split()[0]), item.split()[1].strip()
                if games[game][color] < count:
                    games[game][color] = count

    return sum(map(lambda x: x['red'] * x['green'] * x['blue'],
                   games.values()))


if __name__ == '__main__':

    t_part1(part1)
    t_part2(part2)

    source = load_input('inputs/day2.txt')
    print(
        part1(source, constraint={"red": 12, "green": 13, "blue": 14}),
        part2(source)
    )
