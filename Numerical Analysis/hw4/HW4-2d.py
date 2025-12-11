# assignment4_problem2_d.py
#
# Problem 2(d) 
# ∫_{y=-2}^{2} ∫_{x=0}^{4} (x^2 − 3 y^2 + x y^3) dx dy
#
from scipy.integrate import dblquad
import numpy as np

# Integrand f(x, y) = x^2 − 3 y^2 + x y^3
# Note: dblquad expects the function as f(y, x)
def f(y, x):
    return x**2 - 3.0 * y**2 + x * y**3

# Limits for x: 0 to 4
x_min = 0.0
x_max = 4.0

# Limits for y: -2 to 2 (independent of x)
y_lower = lambda x: -2.0
y_upper = lambda x:  2.0

# Do the double integration
I_val, I_err = dblquad(f, x_min, x_max, y_lower, y_upper)

# Analytical result:
I_exact = 64.0 / 3.0

# True percent relative error
true_percent_relative_error = abs((I_exact - I_val) / I_exact) * 100.0

print("Problem 2(d): dblquad result for the double integrel")
print(f"Numerical value (dblquad): {I_val:.10f}")
print(f"Estimated integration error reported by dblquad: {I_err:.2e}")
print(f"Analytical value: {I_exact:.10f}")
print(f"True percent relative error: {true_percent_relative_error:.6f} %")
