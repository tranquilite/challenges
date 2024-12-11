#Problem 16 - Power digit sum
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

import time as time

start = time.time()
def powersum():
	a = str(2**1000)
	b = []
	for n in a:
		b.append(int (n))
	print(sum(b))

powersum()
print(time.time() - start)
