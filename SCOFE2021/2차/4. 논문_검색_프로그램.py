N = int(input())
sakin = []
for _ in range(N):
    sakin.append(input())

Q = int(input())
srch = []
for _ in range(Q):
    srch.append(input())

# 긴 것부터 검색하며 색인 길이가 더 짧아지는 순간 멈춰 효율 향상
sakin.sort(key=lambda x: len(x), reverse=True)

ans = []
for q in srch:
    an = 0
    for i in sakin:
        if len(q) <= len(i):
            if q in i:
                an += 1
        else:
            break
    ans.append(an)

for a in ans:
    print(a)