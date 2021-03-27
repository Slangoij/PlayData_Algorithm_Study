N = int(input())
maps = list(map(int, input()))

for i in range(2, N):
    if maps[i]:
        maps[i] = maps[i-1] + maps[i-2]

print(maps[-1])