#!/usr/bin/python

from math import sin,cos,tan,log

def cot(x):
    return 1/tan(x)

def f(x):
    return x**2/ sin(x)

def df(x):
    return (2*x - x**2 * cot(x))/sin(x)

hs = [ 10**(-i) for i in range(1,16) ]

def zentralDiff(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)

def fehlerDiff(f, df, x, h):
    return abs(zentralDiff(f, x, h) - df(x))

if __name__ == '__main__':
    for h in hs:
        print("Fehler fuer h = 10**%i" % log(h,10),end="\t")
        print(fehlerDiff(f,df,1,h))
