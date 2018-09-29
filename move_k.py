import sys

print(list(sys.argv[1])[len(list(sys.argv[1])) - int(sys.argv[2]) % len(list(sys.argv[1])):] + list(sys.argv[1])[:len(
    list(sys.argv[1])) - int(sys.argv[2]) % len(list(sys.argv[1]))])
