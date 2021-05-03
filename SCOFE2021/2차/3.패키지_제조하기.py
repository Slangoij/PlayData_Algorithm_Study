N, Q = map(int , input().split())

lst = [0]*(N+1)
for _ in range(N-1):
    up, lo = map(int, input().split())
    if lst[up] == 0:
        lst[up] = [lo]
    else:
        lst[up].append(lo)

ans = []
for _ in range(Q):
    up, lo = map(int, input().split())
    while lst[up] != 0 and lo not in lst[up]:
        up = lst[up]
    if lst[up] != 0 and lo in lst[up]:
            ans.append("yes")
    else:
        ans.append("no")

for an in ans:
    print(an)