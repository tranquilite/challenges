import json

with open('examples/tests.json', 'r') as fh:
    json_testblock = json.load(fh)

DAY = '01'
block = json_testblock[DAY]['part2']
testblock = []
for test in block:
    testblock.append(('\n'.join(test['data']),
                      test['expected']))


def part2test(func):
    """Some real shitty shit"""
    log = []

    for block, expected in testblock:
        _ = func(block.split())
        if _ == expected:
            print('.', end='')
        else:
            print('x', end='')
            log.append(f'>> Got {_}, expected {expected}')
    print()
    for e in log:
        print(e)
