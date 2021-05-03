lst = list(map(int, input().split()))
N, M = lst[0], lst[1]

maps = []
for _ in range(M):
    maps.append(list(map(int, input().split())))

for i in range(M):
    for j in range(N):
        if i and j:
            maps[i][j] += max(maps[i][j-1], maps[i-1][j])
        elif i or j:
            if not i:
                maps[i][j] += maps[i][j-1]
            elif not j:
                maps[i][j] += maps[i-1][j]

print(maps[-1][-1])