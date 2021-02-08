def solution(n, m):
    answer = []
    yac_n = []
    yac_m = []

    for i in range(1, n + 1):
        if not n % i:
            yac_n.append(i)
    for i in range(1, m + 1):
        if not m % i:
            yac_m.append(i)
    yac_n.sort(reverse=True)
    yac_m.sort(reverse=True)

    i = g_yac = 0
    while i < len(yac_n):
        if yac_m.count(yac_n[i]):
            answer.append(yac_n[i])
            g_yac = yac_n[i]
            break
        else:
            i += 1

    answer.append((n * m) / g_yac)
    return answer