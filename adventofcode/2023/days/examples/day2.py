import json

with open('examples/tests.json', 'r') as fh:
    json_testblock = json.load(fh)

DAY = '02'
_block = json_testblock[DAY]


def t_part1(func):
    testblock1 = []
    for test in _block['part1']:
        testblock1.append((test['data'], test['expected']))

    constraint = {"red": 12, "green": 13, "blue": 14}
    log = []
    for block, expected in testblock1:
        ret = func(block, constraint=constraint)
        if ret == expected:
            print('.', end='')
        else:
            print('x', end='')
            log.append(f'>> Got {ret}, expected {expected}')
    print()
    for e in log:
        print(e)


def t_part2(func):
    testblock2 = []
    for test in _block['part2']:
        testblock2.append((test['data'], test['expected']))

    log = []
    for block, expected in testblock2:
        ret = func(block)
        if ret == expected:
            print('.', end='')
        else:
            print('x', end='')
            log.append(f'>> Got {ret}, expected {expected}')
    print()
    for e in log:
        print(e)
