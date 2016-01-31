from time import sleep
fib = 1
fib2 = 2
fibsum = 0
while fib < 4000000:
    if fib % 2 == 0:
        fibsum += fib
    if fib2 % 2 == 0:
        fibsum += fib2
    fib = fib + fib2
    fib2 = fib2 + fib
print fibsum
