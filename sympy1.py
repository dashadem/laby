from sympy.matrices import  zeros
from sympy import symbols
M = zeros(9,9)
l, q, m = symbols("l q m")
M[3,0] = -(l + 2* m)
M[6,0], M[8,0], M[0,3], M[1, 4], M[2, 5] = -l, -l, -1/q, -1/q, -1/q
M[4, 1], M[5, 2] = -m, -m
print(M.eigenvals())