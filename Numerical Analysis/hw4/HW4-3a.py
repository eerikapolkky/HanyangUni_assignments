import numpy as np

def f(x):
    return x * np.exp(2*x)

# trapezoid formula
def T(f, a, b, n):
    h = (b - a) / n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

# Romberg table
a = 0
b = 3
max_k = 6
R = np.zeros((max_k, max_k))

# fill first column with trapezoid results
for i in range(max_k):
    n = 2**i
    R[i,0] = T(f, a, b, n)

# extrapolate
for j in range(1, max_k):
    for i in range(max_k - j):
        R[i,j] = (4**j * R[i+1,j-1] - R[i,j-1]) / (4**j - 1)

print("Romberg table:")
print(R)
print("Romberg result:", R[0,3])

E_t = (504.5359919-R[0,3])/504.5359919*100
print("True percent relative error:", E_t)