import cmath
import time
import numpy as np
from numpy.random import rand


def symmetricDFT(padded):
    M, N = np.shape(padded)
    dft2d = np.zeros((M, N), dtype=complex)
    for k in range(int(M / 2) + 1):
        for l in range(N):
            sum_matrix = 0.0
            for m in range(M):
                for n in range(N):
                    e = cmath.exp(- 2j * np.pi * (float(k * m) / M + float(l * n) / N))
                    sum_matrix += padded[m, n] * e
            dft2d[k, l] = sum_matrix
            if k > 0 and l > 0:
                dft2d[N - k, N - l] = sum_matrix.real + (-1j) * sum_matrix.imag
            elif l == 0 and 0 < k < N - 1:
                dft2d[N - k, l] = sum_matrix.real + (-1j) * sum_matrix.imag

    return dft2d


dim = int(input("Input Square Matrix Length: "))
input_matrix = np.int_(rand(dim, dim) * 256)
start = time.time()
res = symmetricDFT(input_matrix)
end = time.time()
print('Time taken to compute: {} in seconds since the epoch'.format(end - start))

print("--------Symmetric DFT Matrix--------")
print(res)