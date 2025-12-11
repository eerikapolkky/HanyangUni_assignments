import math

def divide_and_average_sqrt(a, tol_percent=0.0001, max_iter=10_000):
    """
    Compute sqrt(a) using the classic divide-and-average iteration:
        x_{i+1} = (x_i + a/x_i)/2
    Stop when the approximate relative change |(x_{i+1}-x_i)/x_{i+1}|*100 < tol_percent.
    For a < 0, return 1j * sqrt(|a|) as a complex number, computed by the same iteration on |a|.
    """
    if a == 0:
        return 0.0, 0, 0.0
    if a < 0:
        val_pos, iters, ea = divide_and_average_sqrt(-a, tol_percent, max_iter)
        return 1j*val_pos, iters, ea

    # initial guess: a reasonable positive starting point
    x_old = a if a > 1 else 1.0
    for i in range(1, max_iter+1):
        x_new = 0.5*(x_old + a/x_old)
        ea = abs((x_new - x_old)/x_new)*100.0
        if ea < tol_percent:
            return x_new, i, ea
        x_old = x_new
    return x_new, max_iter, ea

def main():
    tol = 0.0001  # percent
    tests = [2, 10, -3]
    for a in tests:
        root, iters, ea = divide_and_average_sqrt(a, tol_percent=tol)
        print(f"a = {a:>4}: sqrt ≈ {root} (iterations = {iters}, approx rel change = {ea:.6g}%)")
        # Compare to Python's math for positive a
        if a >= 0:
            print(f"  math.sqrt reference: {math.sqrt(a)}")
        else:
            ref = 1j*math.sqrt(-a)
            print(f"  reference (imag):    {ref}")
    print('\\nDone.')
    
if __name__ == "__main__":
    main()
