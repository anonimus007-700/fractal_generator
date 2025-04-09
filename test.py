import ctypes

# Load the shared library
lib = ctypes.CDLL('./lib.so')

# Define the function signature
my_func = lib.julia_quadratic
my_func.argtypes = [
        ctypes.c_int, ctypes.c_int,
        ctypes.c_float, ctypes.c_float,
        ctypes.c_int
]
my_func.restype = ctypes.c_int

# Pass 5 variables to the function
arg1 = 1000
arg2 = 1000
arg3 = -0.4319
arg4 = 0.6597
arg5 = 100

result = my_func(arg1, arg2, arg3, arg4, arg5)

print("Result:", result)

def julia_quadratic(zx, zy, cx, cy, threshold):
    z = complex(zx, zy)
    c = complex(cx, cy)

    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:
            return i

    return threshold - 1
print(julia_quadratic(arg1, arg2, arg3, arg4, arg5))

import subprocess

command = ['./lib', '12345', 'hello', '123', '12', '1']

result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print("Captured Output:")
print(result.stdout)
print("Error (if any):")
print(result.stderr)
