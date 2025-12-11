import numpy as np

t = np.array([0, 4, 8, 12, 16, 20], float)
y = np.array([67.38, 74.67, 82.74, 91.69, 101.60, 112.58], float)

# linerization: ln y = ln A + k t
p = np.polyfit(t, np.log(y), 1)   # [k, lnA]
k = p[0]
A = np.exp(p[1])

# prediction t = 35
t_pred = 35
y_pred = A * np.exp(k * t_pred)

print("A =", A)
print("k =", k)
print("y(35) =", y_pred)
