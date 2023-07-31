#!/usr/bin/python
### Fibonacci using DP(bottom up) and recursive technique

import sys

def fibonacci(n):
    fib=[]
    fib.append(0)
    fib.append(1)
    for i in range(2,n):   
        next=fib[i-1]+fib[i-2]
        fib.append(next)
    return fib

def recursive_fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return recursive_fib(n-1)+recursive_fib(n-2)    

if __name__ == "__main__":
    n=int(sys.argv[1])
    print(fibonacci(n))
    print(recursive_fib(n))
