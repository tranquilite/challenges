import argparse
import time
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('-L', '--load', action='store_true')
parser.add_argument('-S', '--save', action='store_true')

primes, seed = [], 2


def find_prime(index: int):
    try:
        global seed  # OH GOD
        it = 0
        cycle_start = time.time()
        while len(primes) <= 10001:
            non_primality = 0
            for x in range(2, seed):
                escape = False
                for y in range(2, seed):
                    if (x*y) == seed:
                        non_primality += 1
                        escape = True
                        break
                if escape == True:
                    break

            if non_primality == 0:
                primes.append(seed)

            seed += 1
            it += 1
            if it == 500:
                print(f'{time.time()-cycle_start} - {seed}: {primes}')
                it = 0
                cycle_start = time.time()
    except KeyboardInterrupt:
        if args.save is True:
            with open('euler7.bin', mode='wb') as fhandle:
                pickle.dump( {
                    'seed': seed,
                    'primelist': primes
                }, fhandle)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.load is True:
        with open('euler7.bin', mode='rb') as fhandle:
            swag = pickle.load(fhandle, encoding='bytes')
    #print(args.save)
    #find_prime(10001)

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# OEIS: 104743 or 104759 
# 1,7 10,7 30,2 52,2 102,2 167 198,2 315
