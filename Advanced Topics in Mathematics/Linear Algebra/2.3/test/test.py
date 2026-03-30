
import numpy as np
from sympy import Matrix, pprint

# Define your matrix (example: a 3x4 augmented matrix)
# The matrix is entered as a list of lists, where each inner list is a row
A = Matrix([
    [1,-5,-7,-2],
    [-3,7,5,-2],
])

pprint(A.rref()[0]) 

print(3+2)