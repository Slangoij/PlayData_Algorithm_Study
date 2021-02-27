def solution(n):
    answer = 0
    soo = [True for _ in range(0, n + 1)]

    for i in range(2, int(n ** (1 / 2)) + 2):
        if not soo[i]:
            continue
        j = i * 2
        while j <= n:
            if soo[j]:
                soo[j] = False
            j += i

    for i in range(2, n + 1):
        if soo[i]:
            answer += 1

    return answer