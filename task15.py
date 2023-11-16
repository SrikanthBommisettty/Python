# 14) Write a python program to define a module to find Fibonacci Numbers and import the module to another program.

def fib(n):
    a=0
    b=1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b

