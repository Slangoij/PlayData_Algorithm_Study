def solution(arr, divisor):
    answer = []

    for ar in arr:
        if not ar % divisor:
            answer.append(ar)

    if not len(answer):
        answer.append(-1)

    answer.sort()

    return answer