import matplotlib.pyplot as plt
from math import log


def matrixMult(x,y):
    """multipliziere 2 matrizen"""

    (zeilenx, spaltenx) = dimensionen(x)
    (zeileny, spalteny) = dimensionen(y)

    if not spaltenx == zeileny:
        raise Exception("Matrix x hat nicht die selbe Spaltenanzahl "
                        "wie Matrix y")

    z = initMatrix(zeilenx,spalteny)

    for i in range(0,zeilenx):
        for j in range(0,spalteny):
            # berechne z[i][j]
            s = 0
            for k in range(0,spaltenx):
                s += x[i][k] * y[k][j]
            z[i][j] = s
    return z


def maxNorm(m):
    """Berechne die Maxnorm einer Matrix"""

    i = 0
    
    for zeile in m:
        for elem in zeile:
            i = max(i,abs(elem))
    return i

def dimensionen(x):
    """ermittle die Dimension einer Matrix
    """
    if not isRect(x):
        raise Exception("Matrix x ist nicht rechteckig")

    n = len(x)
    m = len(x[1])

    return (n,m)


def skalarMult(a,r):
    """Fuehrt Multiplikation einer Matrix m mit einem Skalar r durch"""

    (n,m) = dimensionen(a)
    
    # b ist die rueckgabematrix
    b = initMatrix(n,m)

    # iterieren ueber die matrix mit elementweiser multiplikation
    for i in range(0,n):
        for j in range(0,m):
            b[i][j] = a[i][j] * r
    return b


def matrixAdd (a,b):
    """Addition von 2 Matrizen 
    """
    (x1,x2) = dimensionen(a)
    (y1,y2) = dimensionen(b)

    if x1 != y1:
        raise Exception("Die Matrizen haben Unterschiedliche Hoehe")

    if x2 != y2:
        raise Exception("Die Matrizen haben Unterschiedliche Laengen")

    c = initMatrix(x1,x2)
    
    for i in range(0,x1):
        for j in range(0,x2):
            c [i][j] = a[i][j] + b[i][j]
            
    return c


def initMatrix(g,h):
    """Erzeuge neue Matrix mit n Zeilen und m Spalten"""
    return [ [ 0 for x in range(0,h)] for y in range(0,g)]

def isSquare(M):
    """Ueberprueft, ob eine Matrix M quadratisch ist und liefert einen
    entsprechenden Bool zurueck.  Liefert True fuer leere Listen."""
    n = len(M)
    for l in M:
        if len(l) != n:
            return False
    return True


def isRect(M):
    """Ueberprueft, ob eine Matrix M rechteckig ist"""
    if len(M) == 0:
        return True
    else:
        l = len(M[1])
        for x in M:
            if len(x) != l:
                return False
        return True


def iteration(x0, schritte):
    """Fuehre die geforderte Iteration durch

    x0 :: der startvektor fuer die iteration
    schritte :: gibt die anzahl der schritte an, die ausgefuehrt
                werden soll
    """

    (zeilen, spalten) = dimensionen(x0)

    if (zeilen != 2) and (spalten != 1):
        raise Exception("Der Startwert x0 ist kein Spaltenvektor der Laenge 2")

    loesung = [x0]
    for i in range(0,schritte):
        x = loesung[-1]
        loesung.append(schritt(x))
    return loesung[1:]


def loesung():
    return iteration([[1],[3]], 10)


def plotDifferenz(show=True, save=None):
    # kontraktionsfaktor
    l = 0.9
    # maximales k, es wird kmax-mal iteriert
    kmax = 10
    # x_ks ist die liste der ersten kmax x
    x_ks = iteration([[1], [3]], kmax+1)
    dists = []
    ks = range(0,kmax)
    # errechne abstaende
    for k in ks:
        diff = matrixAdd(x_ks[k], skalarMult(x_ks[k+1], -1))
        
        dists.append(log(10,maxNorm(diff)))
    # plotte log l
    ls = []
    for i in ks:
        ls.append(log(l,10))
    plt.plot(ks,ls,'b',ks,dists,'r',)
    plt.legend(["$\log_{10} \| x_{k+1} - x_k \|_\infty$",
                "$\log_{10} l$"])
    plt.xlabel("k")
    if not save is None:
        plt.savefig(filename=save, format='png')
    if show:
        plt.show()


def plotVektorListe(vecs,show=True,save=None):
    """plotte eine Liste von (2,1)-Matrizen in ein Koordinatensystem"""
    xs = []
    ys = []

    for v in vecs:
        xs.append(v[0][0])
        ys.append(v[1][0])

    plt.plot(xs,ys)
    plt.xlabel("1. Komponente")
    plt.ylabel("2. Komponente")
    if not save is None:
        plt.savefig(filename=save,format='png')
    if show:
        plt.show()


def schritt(x):
    """Fuehre iterationsvorschrift aus"""

    if dimensionen(x) != (2,1):
        raise Exception("x hat nicht die Dimensionen (2,1)")

    ma = [ [0.2, -0.7], [0.9, 0] ]
    mb = [ [1.3], [0.3] ]

    return matrixAdd( matrixMult(ma,x), mb)

if __name__ == '__main__':
    plotDifferenz(show=False,save="uebung2_2_kontraktion.png")
    plotVektorListe(loesung(),show=False,save="uebung2_2.png")
