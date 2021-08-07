from numpy import mat
from numpy import random

# gen random 4*4 matrix
rand_mat = mat(random.rand(4, 4))
print(type(rand_mat))
print(rand_mat)

# get inverse matrix
inv_rand_mat = rand_mat.I

result_matrix = rand_mat * inv_rand_mat
print(result_matrix)
