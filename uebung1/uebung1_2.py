#!/usr/bin/python3

A = [ [ 4,-1, 0,-1, 0, 0, 0, 0, 0],
      [-1, 4,-1, 0,-1, 0, 0, 0, 0],
      [ 0,-1, 4,-1, 0,-1, 0, 0, 0],
      [-1, 0,-1, 4,-1, 0,-1, 0, 0],
      [ 0,-1, 0,-1, 4,-1, 0,-1, 0],
      [ 0, 0,-1, 0,-1, 4,-1, 0,-1],
      [ 0, 0, 0,-1, 0,-1, 4,-1, 0],
      [ 0, 0, 0, 0,-1, 0,-1, 4,-1],
      [ 0, 0, 0, 0, 0,-1, 0,-1, 4]
  ]


def diagonalDominant(M):
    """ueberprueft, ob eine quadratische Matrix diagonal dominant ist"""
    if not isSquare(M):
        raise Exception("Matrix M ist nicht quadratisch")
    for i in range(0,len(M)):
        summe = 0
        for j in range(0,len(M)):
            if i != j:
                summe += abs(M[i][j])
        if summe >= M[i][i]:
            return False
    return True                


def jacobi(M, b, tol=10**(-5)):
    """Diese Methode loest das Gleichungssystem, dass durch die Matrix M
    und den Vektor b beschrieben wird, mit Mx = b.

    Argumente:
    M: M ist eine (n x n) Matrix.  Sie beschreibt die Koeffizienten eines 
       linearen Gleichungssystems.
    b: Ist der konstante Teil der Gleichungen des LGS, in einem n-dimensionalen 
       Vektor beschrieben.
    tol: Ist die gewuenschte Genauigkeit.

    Rueckgabewerte:
    Die Funktion uebergibt ein Paar (x,c), wobei x der Loesungsvektor ist und c
    die Anzahl der benoetigten Iterationen.
    """
    # Ueberpruefen, ob die Dimensionen stimmen
    if not isSquare(M):
        raise Exception("Koeffizientenmatrix M ist nicht quadratisch.")
    if len(M) != len(b):
        raise Exception("Dimensionalitaet von b ist verschieden zur Breite der Matrix M.")

    # Wir brauchen einen Startwert fuer das Jacobi-Verfahren
    x_alt = [1 for x in b]
    count = 0
    while True:
        count += 1
        x = b.copy()
        for i in range(0,len(x)):
            for j in range(0,len(x)):
                if i != j:
                    x[i] -= M[i][j]*x_alt[j]
            x[i] = x[i]/M[i][i]
        # print("x : ")
        # printMatrix([x])
        # print("x_alt : ")
        # printMatrix([x_alt])
        if checkTol(x_alt,x,tol):
            return (x,count)
        x_alt = x.copy()


def loesung(gamma,b):
    m = matrixadd(A,skalarMult(einheit(len(A)),gamma))
    return jacobi(m,b)
    

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


def checkTol(a,b,tol):
    """Ueberprueft ob die Elemente von zwei Vektoren sich nur um eine
    gegebene Toleranz unterscheiden.

    Liefert True zurueck, wenn die Werte innerhalb des
    Tolleranzbereiches tol liegen, ansonsten False.
    """
    if len(a) != len(b):
        raise Exception("Vektor a und b haben unterschiedliche laengen")

    for i in range(0,len(a)):
        if abs(a[i] - b[i]) >= tol:
            return False
    return True


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

def dimensionen(x):
    """ermittle die Dimension einer Matrix
    """
    if not isRect(x):
        raise Exception("Matrix x ist nicht rechteckig")

    n = len(x)
    m = len(x[1])

    return (n,m)

def matrixadd (a,b):
    """Addition von 2 Matrizen 
    """
    (x1,x2) = dimensionen(a)
    (y1,y2) = dimensionen(b)

    if x1 != x2:
        raise Exception("Die Matrizen haben Unterschiedliche Hoehe")

    if y1 != y2:
        raise Exception("Die Matrizen haben Unterschiedliche Laengen")

    c = initMatrix(x1,x2)
    
    for i in range(0,x1):
        for j in range(0,x2):
            c [i][j] = a[i][j] + b[i][j]
            
    return c


def initMatrix(g,h):
    """Erzeuge neue Matrix mit n Zeilen und m Spalten"""
    return [ [ 0 for x in range(0,h)] for y in range(0,g)]

def einheit(n):
    """Erzeugt eine Einheitsmatrix der groesze n*n"""
    e = []
    # erzeuge n*n Matrix mit nur Nullen
    e = initMatrix(n,n)
    # schreibe 1en in die diagonale der Matrix
    for i in range(0,n):
        e[i][i] = 1
    return e


def printMatrix(m):
    """Gebe eine Matrix auf stdout aus"""
    for l in m:
        for e in l:
            print(e,end='\t')
        print('')
