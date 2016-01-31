import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
large = 0
prmlrg = 2
while prmlrg * prmlrg <= 600851475143:
    if is_prime(prmlrg) and 600851475143 % prmlrg == 0:
        large = prmlrg
        print large
    prmlrg = prmlrg + 1
print large
print "done"