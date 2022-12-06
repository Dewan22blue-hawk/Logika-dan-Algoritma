# from math import factorial
# from math import pow
# import defef as denny

# print(denny.penjumlahan(7, 8))

# oangjat = pow(3, 2)
# print(oangjat)

# a = int(input("nilai = "))
# fuck = factorial(a)
# print(fuck)

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(100)
