import math


def solution(n, a, b):
    tmpbin = int(bin(a)[2:]) ^ int(bin(b)[2:])

    for i in range(int(math.log2(n)), 0, -1):
        if tmpbin & (1 << i):
            return i