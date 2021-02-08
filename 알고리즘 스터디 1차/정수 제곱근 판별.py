import math


def solution(n):
    answer = 0
    tmp = int(math.sqrt(n))
    if tmp ** 2 == n:
        m = tmp
        answer = (m + 1) ** 2
    elif (tmp + 1) ** 2 == n:
        m = tmp + 1
        answer = (m + 1) ** 2
    else:
        answer = -1

    return answer