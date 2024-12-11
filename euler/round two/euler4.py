# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

top = 0

for x in range(100,999):
    for y in range(100,999):
        temp = x * y
        temp_list = str(temp)
        if temp_list == temp_list[::-1]:
            if temp > top:
                print(top)
                top = temp

print(top)
