#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, x: List[int], y: List[int]) -> int:
def solve(N, M, x, y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    x = [None for _ in range(M)]
    y = [None for _ in range(M)]
    for i in range(M):
        x[i], y[i] = map(int, input().split())
    a = solve(N, M, x, y)
    print(a)

if __name__ == '__main__':
    main()
