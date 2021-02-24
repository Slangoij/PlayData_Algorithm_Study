def solution(n):
    answer = 0
    new_n = list(bin(n)[2:])

    return new_n.count('1')