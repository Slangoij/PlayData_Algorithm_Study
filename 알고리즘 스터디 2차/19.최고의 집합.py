def solution(n, s):
    if n > s:
        return [-1]
    else:
        answer = [s // n] * n
        s -= (s // n) * n
        while s:
            answer[s] += 1
            s -= 1
        answer.sort()

        return answer