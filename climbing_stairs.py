import sys

x = lambda t: 1 if t == 0 else 0 if t < 0 else x(t - 1) + x(t - 2)
print(x(int(sys.argv[1]) - 1) + x(int(sys.argv[1]) - 2))
