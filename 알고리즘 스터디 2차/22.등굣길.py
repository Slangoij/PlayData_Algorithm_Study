def solution(m, n, puddles):
    # 초기 맵 설정
    maps = [[0]*m for _ in range(n)]
    for x, y in puddles:
        maps[y-1][x-1] = -1

    if n > 1:
        for i in range(n):
            if maps[i][0] == -1:
                break
            maps[i][0] = 1
    if m > 1:
        for i in range(m):
            if maps[0][i] == -1:
                break
            maps[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] != -1:
                if maps[i-1][j] != -1:
                    maps[i][j] += maps[i-1][j]
                if maps[i][j-1] != -1:
                    maps[i][j] += maps[i][j-1]

    return maps[-1][-1]%1000000007


mm = 4
nn = 3
puddless = [[2,2]]


print(solution(mm, nn, puddless))

mm = 1
nn = 5
puddless = [[1,2]]