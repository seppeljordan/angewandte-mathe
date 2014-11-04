#!/usr/bin/python
# Mark Schatz - 545097, Sebastian Jordan - 538134

from math import sin,cos,tan,log

def cot(x):
    """Cotangens einer Zahl x"""
    return 1/tan(x)

def f(x):
    """f repraesentiert die abzuleitende Funktion"""
    return x**2/ sin(x)

def df(x):
    """df  repraesentiert die analytische Ableitung der Funktion f"""
    return (2*x - x**2 * cot(x))/sin(x)

# hs definiert eine Liste mit den geforderten h
hs = [ 10**(-i) for i in range(1,16) ]

def zentralDiff(f, x, h):
    """berechne den zentralen Differenzenquotienten

    Argumente:
    f: ist die Funktion ueber die der Differenzenquotient berechnet werden soll
    x: ist die Stelle an der der Differenzenquotient berechnet werde soll.
    h: ist die Differenz, die zur Berechnung benutzt wird.
    """
    return (f(x+h) - f(x-h))/(2*h)

def fehlerDiff(f, df, x, h):
    """Berechnet den Fehler des Diffrenzenquotienten zur analytischen Ableitung

    f: ist die Funktion auf der der Differenzenquotient berechnet werden soll
    df: ist die analytische Ableitung der Funktion f
    x: ist die Stelle an der der Fehler ermittelt werden soll
    h: ist die Differenz mit der der Differenzenquotient ermittelt werden soll
    """
    return abs(zentralDiff(f, x, h) - df(x))

if __name__ == '__main__':
    for h in hs:
        print("Fehler fuer h = 10**%i" % log(h,10),end="\t")
        print(fehlerDiff(f,df,1,h))
