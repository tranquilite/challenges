import json
import io
import sys
import time


def test_aoc(day: str, part: str, *,
             tests='examples.json',
             timer: bool = False,
             run_test: bool = False):
    """
    Quick and shitty decorator to ease my suffering (run "tests")
    Recycled from my AoC 2023-attempt (and modified, d'oh).
    day: str
    part: str - key to test set
    tests: str - name of test battery
    timer: bool - print runtime
    """

    def decorator(func):
        with open(tests, 'r') as fh:
            _block = json.load(fh)
        if day not in _block or part not in _block[day]:
            return lambda x: None  # fugly hack
        else:
            _block = _block[day]

        def wrapper(*args, **kwargs):
            if run_test is False:
                return func(*args, **kwargs)
            print(f'Running {func.__name__} (day {day})')

            wrapped_output = io.StringIO()  # fake print-buffer
            testblock, log, ret = [], [], None

            for test in _block[part]:
                testblock.append((test['input'], test['expected']))

            for idx, testset in enumerate(testblock):
                block, expected = testset[0], testset[1]
                try:
                    sys.stdout = wrapped_output  # capture print()
                    # why? Because I print()-debug, and my window's full
                    starttime = time.time()
                    if block == "aoc":  # if block is raw, call with passed
                        ret = func(*args, **kwargs)
                    else:  # if not, assume *test* block
                        ret = func(lines=block,  **kwargs)
                    stoptime = time.time()
                    if timer:
                        log.append(f'>> Case {idx}: Ran in {stoptime-starttime} secs')

                except Exception as err:  # yolo
                    log.append(f'>> Case {idx}: Met {err}')
                finally:
                    sys.stdout = sys.__stdout__  # release print()
                    if ret == expected:
                        print('.', end='')  # stole this from unittest. pretty.
                    else:
                        print('x', end='')
                        log.append(f'>> Case {idx}: got {ret}, expected {expected}')

            print()
            for e in log:
                print(e)

            print(wrapped_output.getvalue())  # dump fake print buffer

            return ret
        return wrapper
    return decorator
