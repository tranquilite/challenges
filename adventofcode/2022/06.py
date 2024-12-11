# --- Day 6: Tuning Trouble ---

def day6(datastream: str, distinct=4) -> int:
    stream_size = len(datastream)

    for idx in range(stream_size):
        subset = set(datastream[idx:idx+distinct])
        if len(subset) == distinct:
            return idx+distinct
    return False


if __name__ == '__main__':
    tests = [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)
    ]

    for test in tests:
        print(day6(datastream=test[0]) == test[1])

    for test in tests:
        print(day6(datastream=test[0], distinct=14) == test[2])

    with open('inputs/day6.txt', mode='r') as fh:
        setup = fh.readlines()

        print(day6(datastream=setup[0]))
        print(day6(datastream=setup[0], distinct=14))
