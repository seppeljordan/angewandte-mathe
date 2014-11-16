import math
from matplotlib import pyplot as plt

def f(x,n):
    return (x - 1)**n

def df(x,n):
    return n*( x - 1 )**(n - 1)

def newton(n,x0=3,tol=0.000001,maxiter=1000):
    step = lambda i: i - (f(i,n)/df(i,n))
    x1 = x0
    accu = 0
    for i in range(0,maxiter+1):
        x1 = step(x0)
        try:
            accu += abs(x1-1)/abs(x0 - 1)
        except ZeroDivisionError:
            # Wenn wir richtig raten, dann ist der Nenner 0
            return (x0,accu/i)
        if abs(x0-x1) < tol:
            mean = accu/(i+1)
            return (x1, mean)
        x0 = x1
    raise Exception("%i Iterationen ohne Ergebnis durchlaufen, Abbruch" % maxiter)

def plotVergleich(show=True, save=None):
    ns = range(1,55)
    ergebnisse = []
    for n in ns:
        ergebnisse.append(newton(n)[1])
    vergleiche = []
    for n in ns:
        vergleiche.append(1-1/n)
    plt.plot(ns,ergebnisse,ns,vergleiche)
    plt.xlabel("$n$")
    plt.legend(["$c_n$","$ 1-\\frac{1}{n} $"],loc='lower right')
    if show:
        plt.show()
    if not save is None:
        plt.savefig(filename=save,format="png")


if __name__ == '__main__':
    plotVergleich(show=False,save="uebung2_2_newton_vergleich.png")
