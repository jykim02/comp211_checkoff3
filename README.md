# comp211_checkoff3

## Introduction
The topic I chose to explore for the third checkoff was about Python Libraries Implemented in C. The motivation was to better understand how libraries like NumPy can achieve high performance by implementing computationally intensive operations in C. I then investigated how Python programs can call functions written in C, and benchmarked my approach to NumPy, as well as functions written in Python.

## What I chose to explore
I chose to explore ctypes, a built-in foreign function library for Python that allows calling functions in DLLs/shared libraries.

## Summarizing Interesting Discoveries
I found that the function in C ran much faster than the one written in Python. For a vector length of 1 million, Python performed ten times worse.

NumPy's `np.dot` was faster than my C implementation at that vector length. My C function adds each product to a single running total. NumPy can use an optimized library for the dot product, which can process several elements at once and keep multiple partial sums before combining them. These optimizations help explain how NumPy can outperform a simple compiled loop. [NumPy `dot` documentation](https://numpy.org/doc/stable/reference/generated/numpy.dot.html)· 

## Run the experiment

To run the project, run these commands from the project directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Compile the C library (on macOS):

```sh
cc -O3 -dynamiclib dot_product.c -o libdot.so
```

Then run:

```sh
python benchmark.py
```

The script only imports `time`, `numpy`, `matplotlib`, and `ctypes`.
The Python function multiplies matching list elements and adds them in a loop.
The C function receives pointers to the same data in NumPy arrays.

Each implementation runs ten times per vector length. The script plots the
average runtimes and saves the graph as `benchmark.png`.
Input preparation happens before timing.

Edit `sizes` in `benchmark.py` to change the vector lengths.
