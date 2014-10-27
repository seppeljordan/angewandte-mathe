import matplotlib.pyplot as plt

from uebung1_3 import *

def plot_uebung1_3():
    fehlers = []
    for x in hs:
        fehlers.append(fehlerDiff(f,df,1,x))
    plt.plot(hs,fehlers)
    plt.axis([min(hs),max(hs),min(fehlers),max(fehlers)])
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
