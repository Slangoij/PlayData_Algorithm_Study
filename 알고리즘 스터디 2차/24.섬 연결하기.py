def solution(n, costs):
    costs.sort(key=lambda x:(x[2], x[0], x[1]))

    con = []
    vstd = [False for _ in range(n)]
    nowcost = costs.pop(0)
    answer = nowcost[2]
    con.extend(nowcost[:2])
    vstd[nowcost[0]] = vstd[nowcost[1]] = True
    while sum(vstd) < n:
        for cost in costs:
            if cost[0] in con and cost[1] in con:
                continue
            elif cost[0] in con or cost[1] in con:
                if cost[0] not in con:
                    answer += cost[2]
                    vstd[cost[0]] = True
                    con.append(cost[0])
                elif cost[1] not in con:
                    answer += cost[2]
                    vstd[cost[1]] = True
                    con.append(cost[1])
                costs.remove(cost)
                break

    return answer


# n = 5
# costs = [[0,1,1],[3,4,1],[1,2,2],[2,3,4]]
# print(solution(n, costs))

# n = 5
# costs = [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]
# print(solution(n, costs))

# n = 3
# costs = [[1,0,1], [0,2,1]]
# print(solution(n, costs))

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))

# # 예시답안:
# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x: x[2])
#     visited = [True] + [False] * (n - 1)

#     while not all(visited):
#         for cur_node, next_node, cost in costs:
#             print(visited)
#             if visited[cur_node] and visited[next_node]:
#                 continue
#             if visited[cur_node] or visited[next_node]:
#                 visited[cur_node] = visited[next_node] = True
#                 answer += cost
#                 break
#     return answer


# # 2nd try:
# def solution(n, costs):
#     costs.sort(key=lambda x:(x[2], x[0], x[1]))
#     cost_map = [[0] * (i+1) for i in range(n)]
#     for cost in costs:
#         cost_map[max(cost[:2])][min(cost[:2])] = cost[2]

#     for i in range(2, n):
#         for j in range(n-i):
#             cost_map[i+j][j] += min(cost_map[i+j-1][j], cost_map[i+j][j+1])

#     return cost_map[-1][0]

    # answer = 0
    # costs.sort(key=lambda x:(x[2], x[0], x[1]))
    # vstd = [False] * (n)
    # con = []
    # uncon = []

    # for cost in costs:
    #     if cost[0] in con or cost[1] in con:
    #         if cost[0] not in con:
    #             con.append(cost[0])
    #         if cost[1] not in con:
    #             con.append(cost[1])
                
    #         if not vstd[cost[0]] or not vstd[cost[1]]:
    #             answer += cost[2]
    #             if not vstd[cost[0]]:
    #                 vstd[cost[0]] = True
    #             if not vstd[cost[1]]:
    #                 vstd[cost[1]] = True

    # return answer


# def solution(n, costs):
#     cost_map = [[0] * (i+1) for i in range(n)]

#     for cost in costs:
#         cost_map[max(cost[:2])][min(cost[:2])] = cost[2]

#     for i in range(2, n):
#         for j in range(i):
#             # if j == i-1:
#             #     cost_map[i][j] += cost_map[i-1][j-1]
#             # elif j:
#             #     cost_map[i][j] += min(cost_map[i-1][j-1], cost_map[i-1][j])
#             # else:
#             #     cost_map[i][j] += cost_map[i-1][j]

#             if cost_map[i][j]:
#                 # if j:
#                 #     cost_map[i][j] += min(cost_map[i-1][j-1], cost_map[i-1][j])
#                 if j == i-1:
#                     cost_map[i][j] += cost_map[i-1][j-1]
#                 elif j:
#                     cost_map[i][j] += min(cost_map[i-1][j-1], cost_map[i-1][j])
#                 else:
#                     cost_map[i][j] += cost_map[i-1][j]

#         # nowlst = cost_map[i][:i]
#         # tmplst = []
#         # for j in nowlst:
#         #     if j:
#         #         tmplst.append(j)
#         # answer += min(tmplst)
    
#     answer = []
#     for i in cost_map[-1]:
#         if i:
#             answer.append(i)

#     return min(answer)