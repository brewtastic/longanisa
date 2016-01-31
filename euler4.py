def palindrome(num):
    return str(num) == str(num)[::-1]

total = 0

for i in xrange(99,999):
    for l in xrange(99,999):
        big = i * l
        if palindrome(big):
            if big > total:
                total = big
print total
