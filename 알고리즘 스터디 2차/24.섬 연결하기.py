def solution(n, costs):
    answer = 0

    cost_map = [[0] * n for _ in range(n)]

    for cost in costs:
        cost_map[min(cost[:2])][max(cost[:2])] = cost[2]

    for i in range(1, n):
        nowlst = cost_map[i][:i]
        tmplst = []
        for j in nowlst:
            if j:
                tmplst.append(j)
        answer += min(tmplst)

    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))