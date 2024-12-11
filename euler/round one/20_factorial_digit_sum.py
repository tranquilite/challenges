# Problem 20 - Factorial digit sum
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

import time as t

start = t.time()
def factorial_sum(f_lengde):
	f_prod = 1
	f_sum = 0
	for n in range(f_lengde,1,-1):
		f_prod = f_prod * n

	for m in str(f_prod):
		f_sum = f_sum + int(m)
	print(f_sum)

factorial_sum(100)
print(t.time() - start)
