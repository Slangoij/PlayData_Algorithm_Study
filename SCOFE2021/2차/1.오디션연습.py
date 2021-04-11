import datetime as dt
from datetime import timedelta as td

inp = input().split()
N, practime = int(inp[0]), dt.datetime.strptime(inp[1], "%H:%M:%S")
zerotime = dt.datetime.strptime("00:00:00", "%H:%M:%S")
lst = []
for i in range(N):
    lst.append(dt.datetime.strptime(input(), "%M:%S"))

practime = (practime - zerotime).seconds
ply_lst = [(i-zerotime).seconds for i in lst]

cnt_lst = [0]*N
for i in range(len(cnt_lst)):
    lft_time = practime
    idx, cnt = i, 0
    while lft_time>0 and idx<N:
        lft_time -= ply_lst[idx]
        idx+=1
        cnt += 1
    cnt_lst[i] = cnt

print(max(cnt_lst), cnt_lst.index(max(cnt_lst))+1)

# 2 00:00:01
# 00:00
# 00:00