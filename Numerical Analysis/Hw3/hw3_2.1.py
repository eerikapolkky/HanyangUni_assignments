import numpy as np

t = np.array([0,4,8,12,16,20], float)
y = np.array([67.38,74.67,82.74,91.69,101.60,112.58], float)

# Linear
a1, a0 = np.polyfit(t, y, 1)
y_lin = a0 + a1*t
SSE_lin = np.sum((y - y_lin)**2)

# Quadratic
c, b, a = np.polyfit(t, y, 2)
y_quad = a + b*t + c*t**2
SSE_quad = np.sum((y - y_quad)**2)

# Exponential
k, lnA = np.polyfit(t, np.log(y), 1)
A = np.exp(lnA)
y_exp = A*np.exp(k*t)
SSE_exp = np.sum((y - y_exp)**2)

print(a0, a1, SSE_lin)
print(a, b, c, SSE_quad)
print(A, k, SSE_exp)
