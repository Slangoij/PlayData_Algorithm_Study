# 틀린 답으로 제출 후 완료
tmp_lst = list(map(int, input().split()))
N, M = tmp_lst[0], tmp_lst[1]

maps = []
for _ in range(M):
    maps.append(list(input()))

c_idx = []
find_idx = 0
c_cnt = maps[0].count('c')
for _ in range(c_cnt):
    c_idx.append(maps[0].find('c', find_idx))
    find_idx = maps[0].find('c', find_idx)

ans_lst = [0] * c_cnt
tmp_ans = 0

def solution():
    for c in range(c_cnt):
        j = c_idx[c]
        for i in range(M-2):
            nxtstep = [True] * N
            for k in range(N):
                if maps[i+1][k] == 'x':
                    nxtstep[k] = False
                if maps[i+2][k] == 'x':
                    nxtstep[k] = False
            if sum(nxtstep) == 0:
                return '-1'
            nxtj = N
            for k in range(N):
                if k != j and maps[i+1][k] != 'x':
                    nxtj = min(nxtj, abs(k-j))
            tmp_ans += abs(nxtj-j)
        ans_lst.append(tmp_ans)
    return min(ans_lst)

print(solution())