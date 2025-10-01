#!/usr/bin/env python3
# hw1-1.py — Numerical Analysis HW1, Problem 1
# Divide-and-average (Newton) method for square root with while...break

import math

def newton_sqrt(a, tol_percent=0.0001, max_iter=10000):

    if a == 0:
        return 0.0, 0, 0.0
    if a < 0:
        val_pos, iters, ea = newton_sqrt(-a, tol_percent, max_iter)
        return 1j * val_pos, iters, ea

    x = a if a > 1 else 1.0
    i = 0

    while True:                          # infinite loop, will break out when done
        i += 1
        x_new = 0.5 * (x + a / x)             #divide and average
        ea = abs((x_new - x) / x_new) * 100.0        #relative error in percent

        if ea < tol_percent or i >= max_iter:
            x = x_new
            break

        x = x_new
        
    return x, i, ea


if __name__ == "__main__":
    tol = 0.0001                       #making results more simplier to read
    for a in (2, 10, -3):
        root, iters, ea = newton_sqrt(a, tol_percent=tol)
        print(f"a = {a}")
        print(f"  sqrt ≈ {root}")
        print(f"  iterations = {iters}")
        print(f"  last relative change ≈ {ea:.6g} %")
        ref = math.sqrt(a) if a >= 0 else 1j * math.sqrt(-a)
        print(f"  reference = {ref}\n")