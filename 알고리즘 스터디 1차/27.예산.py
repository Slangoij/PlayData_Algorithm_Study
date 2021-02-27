def solution(d, budget):
    answer = 0
    # d_sum = 0
    idx = 0
    d.sort()

    while idx < len(d) and d[idx] <= budget:
        budget -= d[idx]
        idx += 1

    answer = idx
    return answer