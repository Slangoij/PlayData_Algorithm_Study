# 2st try: 다른 사람의 풀이 참고(다이나믹 프로그래밍 활용)
def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            tmplst = []
            for k in range(4):
                if j != k:
                    tmplst.append(land[i-1][k])
            land[i][j] += max(tmplst)

    return max(land[-1])


landd = [
    [1,2,3,5],
    [5,6,7,8],
    [4,3,2,1]]
print(solution(landd))

# # 1st try: 호출 스택 제한이 있어 런타임 에러가 걸린 듯하다. 재귀로 ㄴㄴ
# answer = []
# aland = []
# lst_vst = [False]*4
#
#
# def dfs(now, leng):
#     tmp = 0
#     if now == leng:
#         answer.append(tmp)
#     else:
#         for i in range(4):
#             if not lst_vst[i]:
#                 lst_vst[i] = True
#                 tmp += aland[i]
#                 dfs(now+1, leng)
#                 lst_vst[i] = False
#
#
# def solution(land):
#     global answer, aland
#     aland = land
#     dfs(0, len(land))
#
#     answer.sort(reverse=True)
#
#     return answer[0]

