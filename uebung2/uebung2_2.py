import math

def f(x,n):
    return (x - 1)**n

def df(x,n):
    return (n*( x - 1 ))**(n - 1)

def newton(x0,n,tol):
    step = lambda i: i - (f(i,n)/df(i,n))
    while f(x0,n) > tol:
        x0 = step(x0)
    return x0
