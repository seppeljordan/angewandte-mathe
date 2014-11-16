from uebung2_1 import (matrixMult,
                       matrixAdd,
                       skalarMult,
                       maxNorm)
from math import (sin,cos,atan,sqrt)
from matplotlib import pyplot as plt

def matrixSub(m1,m2):
    return matrixAdd(m1,skalarMult(m2,-1))

def f(p,x1,x2):
    r = p[0][0]
    phi = p[1][0]
    return [ [r*cos(phi) - x1], [r*sin(phi) - x2] ]

def inverseJ(v):
    """berechne inverse jacobimatrix fuer gegebenen phi-r-vektor

    v - ist ein vektor [ [r], [phi] ]
    """
    r = v[0][0]
    phi = v[1][0]
    q = sin(phi) + cos(phi)
    return [ [ cos(phi), sin(phi)],
             [ -sin(phi)/(r), cos(phi)/(r) ] ]

def polar(x1,x2,epsilon=0.000001, maxiter=1000):
    """aproximiert die Polarkoordinaten von kartesischen koordiantes R^2"""
    p = [ [1],[0] ]
    for i in range(0,maxiter+1):
        p1 = matrixSub(p,matrixMult(inverseJ(p),f(p,x1,x2)))
        if maxNorm(matrixSub(p,p1)) < epsilon:
            break
        if i == maxiter:
            import pdb; pdb.set_trace()
            raise Exception("%i Iterationen ueberschritten, Abbruch" % i)
        p = p1
    return (p1[0][0],p1[1][0])
    
def polarListe(x1,x2,epsilon=0.000001, maxiter=1000):
    """aproximiert die Polarkoordinaten von kartesischen koordiantes R^2

    Die Methode gibt eine Liste mit allen Zwischenergebnissen zurueck.
    """
    p = [ [1],[0] ]
    res = [p]
    for i in range(0,maxiter+1):
        p1 = matrixSub(p,matrixMult(inverseJ(p),f(p,x1,x2)))
        res.append(p1)
        if maxNorm(matrixSub(p,p1)) < epsilon:
            break
        if i == maxiter:
            import pdb; pdb.set_trace()
            raise Exception("%i Iterationen ueberschritten, Abbruch" % i)
        p = p1
    return res


def plotDiffs(show=True, save=None):
    phi_genau = atan(2)
    r_genau = sqrt(5)

    norm2 = lambda v: sqrt(v[0][0]**2 + v[1][0]**2)

    # errechne Differenzen
    ergebnisse = []
    for x in polarListe(1,2):
      ergebnisse.append(norm2(matrixSub([[r_genau],[phi_genau]],x)))

    plt.plot(range(0,len(ergebnisse)), ergebnisse)
    plt.xscale('log')
    plt.yscale('log')
    if show:
        plt.show()
    if not save is None:
        plt.savefig(save,format='png')

if __name__ == '__main__':
    plotDiffs(show=False,save="uebung2_3_newton.png")
                
