import numpy as np

N = input()
tmp_maps = []
for _ in range(N):
    tmp_maps.append(list(map(int, input())))
maps = np.array(tmp_maps)

ans = 0
size = []
for siz in range(1, N+1):
    now_range = N - i + 1
    for i in range(now_range):
        for j in range(now_range):
            ans += maps[maps[i:i+siz, j:j+siz]].sum()

print(ans)