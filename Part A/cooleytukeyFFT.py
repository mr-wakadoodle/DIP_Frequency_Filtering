import time
import timeit
from numpy.random import rand
import numpy as np


def naiveDFTImplementation(x):
    x = np.asarray(x, dtype=float)
    dimension = x.shape[0]
    n = np.arange(dimension)
    k = n.reshape((dimension, 1))
    temp = np.exp(-2j * np.pi * k * n / dimension)
    return np.dot(temp, x)


def FFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:
        return naiveDFTImplementation(x)
    else:
        even = FFT(x[::2])
        odd = FFT(x[1::2])
        temp = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([even + temp[:N // 2] * odd, even + temp[N // 2:] * odd])


dim = int(input("Input total number of frequency in matrix must be in power of 2 for computation of "
                "FFT): "))
frequency_samples = np.int_(rand(dim) * 256)
start = time.perf_counter_ns()
res = FFT(frequency_samples)
end = time.perf_counter_ns()
print('Time taken to compute: {} in nanoseconds since the epoch'.format(end - start))

print("--------FFT Computation--------")
print(res)
