#!/bin/python
def polyEval(a, x, n):

    if (n == 0):
        return a[0]
    return (a[n]*pow(x,n))+polyEval(a, x, n-1)
a = [1,1]
n = 1
x = 2

ans = polyEval(a, x, n)
print ans

