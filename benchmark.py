import time
import numpy as np
import matplotlib.pyplot as plt
import ctypes
from dot_product import python_dot


def average_time(function, repeats, *args):
    start = time.perf_counter()
    for _ in range(repeats):
        function(*args)
    return (time.perf_counter() - start) / repeats

c_dot = ctypes.CDLL("./libdot.so").dot_product
double_pointer = ctypes.POINTER(ctypes.c_double)
c_dot.argtypes = [double_pointer, double_pointer, ctypes.c_size_t]
c_dot.restype = ctypes.c_double

sizes = [10, 100, 1000, 10000, 100000, 1000000]
repeats = 10
times = {"Python": [], "C": [], "NumPy": []}

for size in sizes:
    left = np.random.rand(size)
    right = np.random.rand(size)

    # converts the numpy arrays for the specific function
    left_list = left.tolist()
    right_list = right.tolist()
    left_pointer = left.ctypes.data_as(double_pointer)
    right_pointer = right.ctypes.data_as(double_pointer)

    python_average = average_time(python_dot, repeats, left_list, right_list)
    times["Python"].append(python_average)

    c_average = average_time(c_dot, repeats, left_pointer, right_pointer, size)
    times["C"].append(c_average)

    numpy_average = average_time(np.dot, repeats, left, right)
    times["NumPy"].append(numpy_average)

for name, values in times.items():
    plt.loglog(sizes, values, "o-", label=name)

plt.xlabel("Vector length")
plt.ylabel("Time (seconds)")
plt.legend()
plt.savefig("benchmark.png")
plt.show()
