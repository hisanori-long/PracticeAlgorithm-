#!/usr/bin/env python3
# from typing import *

MOD = 1000000007

# def solve(N: str, x: List[str], y: List[str]) -> int:
def solve(N, x, y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = input()
    x = [None for _ in range(N - 1)]
    y = [None for _ in range(N - 1)]
    for i in range(N - 1):
        x[i], y[i] = input().split()
    a = solve(N, x, y)
    print(a)

if __name__ == '__main__':
    main()
