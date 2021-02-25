import math

def solution(brown, yellow):
    answer = []

    # 가로와 세로의 합
    w_h_sum = int(brown / 2 + 2)
    mid = int(math.ceil(w_h_sum / 2))

    for i in range(3, mid + 1):
        if (i - 2) * (w_h_sum - i - 2) == yellow:
            answer = [i, w_h_sum - i]
            break

    return answer

b = 10
y = 2
print(solution(b, y))