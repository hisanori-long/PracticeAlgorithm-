#!/usr/bin/env python3
# from typing import *



# def solve(N: str, M: str, x: List[str], y: List[str]) -> Any:
def solve(N, M, x, y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = input().split()
    x = [None for _ in range(N - 1)]
    y = [None for _ in range(N - 1)]
    for i in range(N - 1):
        x[i], y[i] = input().split()
    ans = solve(N, M, x, y)
    print(ans)  # TODO: edit here

if __name__ == '__main__':
    main()
