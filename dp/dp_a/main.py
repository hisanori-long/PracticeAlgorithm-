#!/usr/bin/env python3
# from typing import *



# def solve(N: int, h: List[int]) -> int:
def solve(N, h):

    min_costs = [100000000000] * N
    min_costs[0] = 0

    for i in range(0, N-1):
        # i + 1
        cost = abs(h[i] - h[i+1]) + min_costs[i]
        if min_costs[i+1] > cost:
            min_costs[i+1] = cost

        # i + 2
        if i + 2 < N: # リストの範囲内であることを確認
            cost = abs(h[i] - h[i+2]) + min_costs[i]
            if min_costs[i+2] > cost:
                min_costs[i+2] = cost

    return min_costs[-1]


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    h = [None for _ in range(N)]
    for i in range(N):
        h[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, h)
    print(a)

if __name__ == '__main__':
    main()
