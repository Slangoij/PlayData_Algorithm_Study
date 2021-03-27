import numpy as np

N = int(input())
tmp_maps = []
for _ in range(N):
    tmp_maps.append(list(map(int, input())))
maps = np.array(tmp_maps)

ans = 0
size = [0] * (N+1)
for siz in range(1, N+1):
    now_range = N - siz + 1
    tmp_ans = 0
    for i in range(now_range):
        for j in range(now_range):
            if np.all(maps[i:i+siz, j:j+siz]):
                tmp_ans += 1
                ans += 1
    size[siz] = tmp_ans
    
print(f'total: {ans}')
for i in range(1, len(size)):
    if size[i]:
        print(f'size[{i}]: {size[i]}')