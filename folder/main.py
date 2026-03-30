import numpy as np
from sympy import Matrix, pprint

# Define your matrix (example: a 3x4 augmented matrix)
# The matrix is entered as a list of lists, where each inner list is a row
A = Matrix([
    [2,4,-1,5,-2],
    [-4,5,3,-8,1],
    [2,-5,-4,1,8],
    [-6,0,7,-3,1]
])

# pprint(A.rref()[0])
pprint(A)