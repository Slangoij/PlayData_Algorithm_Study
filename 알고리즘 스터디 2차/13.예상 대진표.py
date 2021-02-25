import math


def solution(n, a, b):
    cmp_bin = (a-1) ^ (b-1)

    for i in range(int(math.log2(n))-1, -1, -1):
        if cmp_bin & (1 << i):
            return i+1


N = 16
A = 1
B = 8
print(solution(N,A,B))