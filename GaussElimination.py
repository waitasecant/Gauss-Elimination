import numpy as np
import sys


def GaussElimination(A):
    for i in range(n):
        if A[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            print(
                f"\nR{j+1} -> R{j+1} - {round(ratio,2)} * R{i+1}\n")
            for k in range(n+1):
                A[j][k] = A[j][k] - ratio * A[i][k]
            print(f"\n{A.round(2)}\n")
    return A


def BackSubstitution(U, x, b):
    for i in range(n-1, -1, -1):
        x[i] = (b[i]-sum(U[i][j]*x[j] for j in range(i+1, n)))/(U[i][i])
    return x


# Driver
print("\t\t\tGauss Elimination Method")
n = int(input("Enter number of unknowns"))
A = np.zeros((n, n+1))
x = np.zeros(n)
b = np.zeros(n)
print("Enter Augmented Matrix Coefficients")
for i in range(n):
    for j in range(n+1):
        A[i][j] = float(input(f"A[{i}][{j}]="))

for i in range(n):
    b[i] = A[i][n]

np.linalg.matrix_rank(A)
print("\nA =\n", A[:, :n])
print("\nb =\n", b)
print("\nA|b=\n", A)

if np.linalg.matrix_rank(A) != np.linalg.matrix_rank(A[:, :n]):
    print(
        "Since rank A is not equal to rank [A|b]\nTherefore, the system is inconsistent and has no solution.")
else:
    G = GaussElimination(A)
    U1 = G[:, :n]
    print("\nU\n", U1.round(2))
    b = G[:, n]
    print("\nz\n", b.round(2))
    print("\nU|z=\n", G.round(2), "\n")
    X = BackSubstitution(U1, x, b)
    for i in range(n):
        print(f"x{i+1} = {round(X[i],2)}", end="\t")
