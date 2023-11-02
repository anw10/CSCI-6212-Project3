def MVBLN(A, k):
    n = len(A)
    MVNN = [0] * (n + 1)
    MVNN[1] = A[0]

    # Initialize and fill in array for MVNN since m == 0
    for i in range(2, n + 1):
        MVNN[i] = max(MVNN[i - 1], MVNN[i - 2] + A[i - 1])

    # Initialize 2d array to hold our bottom up values
    MVBLN = [[0] * (k + 1) for _ in range(n + 1)]

    # Fill in 2d array for the case where m == 0
    for bc in range(1, n + 1):
        MVBLN[bc][0] = MVNN[bc]

    for m in range(1, k + 1):
        for i in range(1, n + 1):
            MVBLN[i][m] = max(
                MVBLN[i - 1][m],
                MVBLN[i - 1][m - 1] + A[i - 1],
                MVBLN[i - 2][m] + A[i - 1],
            )

    # Backtrack to build array b from our 2d array MVBLN
    b = [0] * n
    b[n - 1] = 99
    i, m = n, k
    while i > 0:
        if MVBLN[i][m] == MVBLN[i - 1][m]:
            b[i - 1] = 0
            i -= 1
        elif m > 0 and MVBLN[i][m] == MVBLN[i - 1][m - 1] + A[i - 1]:
            b[i - 1] = 1
            i -= 1
            m -= 1
        else:
            b[i - 1] = 1
            if i > 2:
                b[i - 2] = 0
            i -= 2

    return MVBLN[n][k], b


# Testing Code
# Provide an array of numbers below
A = [10, 100, 300, 400, 50, 4500, 200, 30, 90]
# Provide your value for k, the number of adjacent 1's allowed in b
k = 2
print(MVBLN(A, k))
