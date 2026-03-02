#!/usr/bin/env python3

import sys

print("=== Command Quest ===")
a = len(sys.argv)
if a <= 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {a}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {a - 1}")
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {a}")
