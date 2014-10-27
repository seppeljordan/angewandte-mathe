import matplotlib.pyplot as plt

from uebung1_3 import *

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
