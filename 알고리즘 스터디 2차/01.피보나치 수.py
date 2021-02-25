def solution(n):
    answer = 0

    fibos = [0, 1]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        for _ in range(n - 1):
            fibos.append(fibos[-1] + fibos[-2])

    return fibos[-1] % 1234567