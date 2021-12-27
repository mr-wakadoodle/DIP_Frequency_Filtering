import time
import numpy as np
import math
from numpy.random import rand


def forward_transform(matrix):
    """Computes the forward Fourier transform of the input matrix
    takes as input:
    matrix: a 2d matrix
    returns a complex matrix representing fourier transform"""
    height = matrix.shape[0]
    width = matrix.shape[1]

    result = np.zeros((height, width))
    result = np.array(result, dtype=complex)
    for u in range(height):
        for v in range(width):
            k = 0

            for i in range(height):
                for j in range(width):
                    exp_D = np.exp(-2 * math.pi * 1J * ((u * i) + (v * j)) / height)
                    k = k + exp_D * matrix[i, j]

            result[u, v] = k

    return result


dim = int(input("Input Square Matrix Length: "))
input_matrix = np.int_(rand(dim, dim) * 256)
start = time.time()
res = forward_transform(input_matrix)
end = time.time()
print('Time taken to compute: {} in seconds since the epoch'.format(end - start))

print("--------DFT Matrix--------")
print(res)
