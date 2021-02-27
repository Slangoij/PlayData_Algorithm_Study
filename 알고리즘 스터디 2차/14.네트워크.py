def dfs(now):
    for i in range(n):
        if com[now][i] and not vstd[i]:
            vstd[i] = True
            dfs(i)


def solution(n, computers):
    answer = 0
    for i in range(n):
        if not vstd[i]:
            vstd[i] = True
            dfs(i)
            answer += 1

    return answer



# n = 3
# com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# vstd = [False] * n

# n = 3
# com = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# vstd = [False] * n

n = 6
com = [
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1]]
vstd = [False] * n


print(solution(n, com))