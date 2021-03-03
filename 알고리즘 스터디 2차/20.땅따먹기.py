answer = []
aland = []
lst_vst = [False]*4


def dfs(now, leng):
    tmp = 0
    if now == leng:
        answer.append(tmp)
    else:
        for i in range(4):
            if not lst_vst[i]:
                lst_vst[i] = True
                tmp += aland[i]
                dfs(now+1, leng)
                lst_vst[i] = False


def solution(land):
    global answer, aland
    aland = land
    dfs(0, len(land))

    answer.sort(reverse=True)

    return answer[0]

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))