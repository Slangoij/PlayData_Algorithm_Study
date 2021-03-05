def solution(m, n, puddles):
    # 초기 맵 설정
    maps = [[0]*m for _ in range(n)]
    maps[0] = [[1]*m]
    for i in range(n):
        maps[i][0] = 1
    for y,x in puddles:
        maps[y][x] = 0

    for i in range(1, m):
        for j in range(1, n):
            if maps[i][j]:
                maps[i][j] += maps[i-1][j]
                if j:
                    maps[i][j] += maps[i][j-1]

    return maps[-1][-1]

mm = 4
nn = 3
puddless = [[2,2]]
print(solution(mm, nn, puddless))