import matplotlib.pyplot as plt

from uebung1_3 import *
from uebung1_2 import loesung

def plot_uebung1_3():
    """Plotte die Werte die in der Aufgabe geforderdert sind als Graph"""
    # fehlers soll die liste der fehler sein.
    fehlers = []
    # erstelle die liste der fehler zum zugehoerigen h
    for x in hs:
        fehlers.append(fehlerDiff(f,df,1,x))
    # erstelle plot fuer die h's und die fehler
    plt.plot(hs,fehlers)
    # lege achsenminima und maxima fest
    plt.axis([min(hs),max(hs),min(fehlers),max(fehlers)])
    # skaliere die axen logrithmisch
    plt.yscale('log')
    plt.xscale('log')
    # beschrifte die achsen
    plt.ylabel('Fehler')
    plt.xlabel('h')
    # zeige den graphen
    plt.show()

def plot_uebung1_2():
    b = [1 for x in range(0,9)]
    gammas = [x/2.0 for x in range(2,40)]
    schritte = []
    for x in gammas:
        m,s = loesung(x,b)
        schritte.append(s)
    # plotte die anzahl der schritte abhaengig von gamma
    plt.plot(gammas, schritte, 'o')
    plt.ylabel('Anzahl der Schritte')
    plt.xlabel('Gamma')
    plt.show()
    
