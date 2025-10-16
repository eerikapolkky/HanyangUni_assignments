
L = [
    [2.8284271, 0.0,       0.0      ],
    [7.0710678, 5.4772256, 0.0      ],
    [5.3033009, 2.2821773, 5.1639778]
]


b = [50.0, 250.0, 100.0]

def forward_sub(L, b):
    n = len(L)
    y = [0.0]*n
    for i in range(n):
        s = 0.0
        for j in range(i):
            s += L[i][j]*y[j]
        y[i] = (b[i] - s)/L[i][i]
    return y

def transpose(A):
    n = len(A)
    m = len(A[0])
    return [[A[j][i] for j in range(n)] for i in range(m)]

def back_sub_upper(U, y):
    n = len(U)
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        s = 0.0
        for j in range(i+1, n):
            s += U[i][j]*x[j]
        x[i] = (y[i] - s)/U[i][i]
    return x

# 1) Ly = b
y = forward_sub(L, b)

# 2) L^T x = y
U = transpose(L)
x = back_sub_upper(U, y)

# Output (few decimals, like slides)
def fmt(v): return f"{v:.6f}"
print("y =", [fmt(v) for v in y])
print("x =", [fmt(v) for v in x])
