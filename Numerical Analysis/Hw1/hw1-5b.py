import math

# Function
def f(x):
    return x**4 + 2*x**3 + 8*x**2 + 5*x

# Golden-section search
def golden_section_search(xl, xu, es=1.0):
    phi = (math.sqrt(5) - 1) / 2  # 0.618...
    d = phi * (xu - xl)

    x1 = xl + (1 - phi) * (xu - xl)
    x2 = xl + phi * (xu - xl)

    f1 = f(x1)
    f2 = f(x2)

    iteration = 0
    while True:
        iteration += 1
        if f1 > f2:
            xl = x1
            x1 = x2
            f1 = f2
            x2 = xl + phi * (xu - xl)
            f2 = f(x2)
        else:
            xu = x2
            x2 = x1
            f2 = f1
            x1 = xl + (1 - phi) * (xu - xl)
            f1 = f(x1)

        # recent optimal point
        xopt = (xl + xu) / 2
        # floating point relative error
        ea = (1 - phi) * (xu - xl) / abs(xopt) * 100

        print(f"Iteration {iteration}: x ≈ {xopt:.6f}, f(x) ≈ {f(xopt):.6f}, εa ≈ {ea:.3f}%")

        if ea < es:
            break

    return xopt, f(xopt), iteration

# Process 
x_min, f_min, iters = golden_section_search(-2, 1, es=1.0)
print(f"\nresult: x ≈ {x_min:.6f}, f(x) ≈ {f_min:.6f}, Iterations: {iters}")
