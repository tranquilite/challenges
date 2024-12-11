# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallest_number = []
iteration = 1
scope = list(range(0, 11))

try:
    while True:
        for _ in scope:
            if iteration % _ == 0:
                pass
            else:
                pass

        iteration += 1

        if len(smallest_number) > 3:
            break

except KeyboardInterrupt:
    print(smallest_number)
