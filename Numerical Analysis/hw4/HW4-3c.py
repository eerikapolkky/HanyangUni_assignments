from scipy.integrate import quad
import numpy as np

f = lambda x: x*np.exp(2*x)

I, err = quad(f, 0, 3)
print("quad:", I)
print("error estimate:", err)
