import math

def f(x):
    return -12 - 21*x + 18*x*x - 2.75*x*x*x

def linspace(a, b, n):
    return [a + (b - a) * i / (n - 1) for i in range(n)]

def ascii_plot(f, xmin=-5.0, xmax=10.0, width=80, height=24, samples=800):
    xs = linspace(xmin, xmax, samples)
    ys = [f(x) for x in xs]
    ymin, ymax = min(ys), max(ys)
    # pad if flat
    if abs(ymax - ymin) < 1e-12:
        ymin -= 1.0
        ymax += 1.0

    # axes positions
    def x_to_col(x):
        return int(round((x - xmin) / (xmax - xmin) * (width - 1)))
    def y_to_row(y):
        return int(round((y - ymin) / (ymax - ymin) * (height - 1)))

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    # draw axes
    ix0 = x_to_col(0.0)
    iy0 = y_to_row(0.0)
    if 0 <= ix0 < width:
        for r in range(height):
            grid[height - 1 - r][ix0] = '|'
    if 0 <= iy0 < height:
        for c in range(width):
            grid[height - 1 - iy0][c] = '-'
    if 0 <= ix0 < width and 0 <= iy0 < height:
        grid[height - 1 - iy0][ix0] = '+'

    # draw function
    for c in range(width):
        x = xmin + (xmax - xmin) * c / (width - 1)
        y = f(x)
        r = y_to_row(y)
        r = max(0, min(height - 1, r))
        grid[height - 1 - r][c] = '*'

    # print plot
    for row in grid:
        print(''.join(row))

def find_graphical_roots(f, xmin=-5.0, xmax=10.0, samples=2000):
    xs = linspace(xmin, xmax, samples)
    ys = [f(x) for x in xs]
    roots = []
    for i in range(len(xs) - 1):
        if ys[i] == 0.0:
            roots.append(xs[i])
        elif ys[i] * ys[i + 1] < 0:
            # linear interpolation
            x0, x1 = xs[i], xs[i + 1]
            y0, y1 = ys[i], ys[i + 1]
            r = x0 - y0 * (x1 - x0) / (y1 - y0)
            roots.append(r)
    # unique-ish and sorted
    roots = sorted(roots)
    uniq = []
    for r in roots:
        if not uniq or abs(r - uniq[-1]) > 1e-6:
            uniq.append(r)
    return uniq

def bisection(f, xl, xu, es=0.1, max_iter=20):
    fl, fu = f(xl), f(xu)
    if fl * fu > 0:
        raise ValueError("No sign change on [xl, xu].")
    xr, ea = None, float("inf")
    for i in range(1, max_iter + 1):
        xrold = xr
        xr = 0.5 * (xl + xu)
        fr = f(xr)
        if xrold is not None and xr != 0:
            ea = abs((xr - xrold) / xr) * 100.0
            if ea <= es:
                break
        if fl * fr < 0:
            xu, fu = xr, fr
        elif fr * fu < 0:
            xl, fl = xr, fr
        else:
            ea = 0.0
            break
    return xr, i, ea

def false_position(f, xl, xu, es=0.1, max_iter=20):
    fl, fu = f(xl), f(xu)
    if fl * fu > 0:
        raise ValueError("No sign change on [xl, xu].")
    xr, ea = None, float("inf")
    for i in range(1, max_iter + 1):
        xrold = xr
        xr = xu - fu * (xl - xu) / (fl - fu)
        fr = f(xr)
        if xrold is not None and xr != 0:
            ea = abs((xr - xrold) / xr) * 100.0
            if ea <= es:
                break
        if fl * fr < 0:
            xu, fu = xr, fr
        elif fu * fr < 0:
            xl, fl = xr, fr
        else:
            ea = 0.0
            break
    return xr, i, ea

if __name__ == "__main__":
    # (a) Graphical (ASCII) roots
    print("ASCII plot of f(x) on [-5, 10]:")
    ascii_plot(f, xmin=-5, xmax=10, width=80, height=24, samples=2000)
    approx_roots = find_graphical_roots(f, xmin=-5, xmax=10, samples=4000)
    print("\nGraphical approx roots:")
    for r in approx_roots:
        print(f"x ≈ {r:.10f}")

    # (b) Bisection and (c) False Position on [-1, 0]
    xl, xu = -1.0, 0.0
    rb, ib, eab = bisection(f, xl, xu, es=0.1, max_iter=20)
    rf, iff, eaf = false_position(f, xl, xu, es=0.1, max_iter=20)

    print("\nBisection on [-1, 0]:")
    print(f"root ≈ {rb:.10f}, f(root) ≈ {f(rb):.3e}, iters = {ib}, ea ≈ {eab:.3f}%")

    print("\nFalse Position on [-1, 0]:")
    print(f"root ≈ {rf:.10f}, f(root) ≈ {f(rf):.3e}, iters = {iff}, ea ≈ {eaf:.3f}%")