def solution(trophies):
    ans = []
    now_max, cnt = trophies[0], 1
    for i in range(1, len(trophies)):
        if now_max < trophies[i]:
            cnt += 1
            now_max = trophies[i]
    ans.append(cnt)
    
    now_max, cnt = trophies[-1], 1
    for i in range(len(trophies)-2, -1, -1):
        if now_max < trophies[i]:
            cnt += 1
            now_max = trophies[i]
    ans.append(cnt)

    return ans