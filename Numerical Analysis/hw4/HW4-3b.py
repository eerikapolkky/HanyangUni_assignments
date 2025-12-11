import numpy as np

def f(x):
    return x*np.exp(2*x)

a, b = 0, 3
x1 = 1.5 - 1.5/np.sqrt(3)
x2 = 1.5 + 1.5/np.sqrt(3)

I = 1.5 * (f(x1) + f(x2))
print("Gauss 2-point:", I)

E_t = (504.5359919-I)/504.5359919*100
print("True percent relative error:", E_t)
