# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.

def chkact(action):
    actlst = action.split(' ')
    num = 0
    if actlst[0] == 'PUT' and actlst[2] == 'INSIDE':
        num = 0
    elif actlst[0] == 'SET' and actlst[2] == 'LOOSE':
        num = 1
    elif actlst[0] == 'SWAP' and actlst[2] == 'WITH':
        num = 2

    if num%2 == 0:
        return num, int(actlst[1]), int(actlst[3])
    else:
        return num, int(actlst[1])

def solution(n, actions):

    # 각 가방 번호를 인덱스로, 만약 가방에 뭔가 담겨있다면
    # 그 내용물을 해당 인덱스 뒤에 리스트로 담고 있는 리스트
    bags = [[]]+[[i+1] for i in range(n)]

    for action in actions:
        if chkact(action)[0] % 2 == 0:
            chk, x, y = chkact(action)
        else:
            chk, x = chkact(action)[0], chkact(action)[1]

        if chk == 0 and len(bags[x]) and len(bags[y])\
                and bags[x][0] == x and bags[y][0] == y:

        elif chk == 1 and bags[x][0] == x:

        elif chk == 2 and len(bags[x]) and len(bags[y])\
                and bags[x][0] == x and bags[y][0] == y:

        else:  # action이 틀리거나 유효하지 않다면 -1 반환
            return -1

    answer = 0
    for bag in bags:
        if len(bag):
            answer += 1

    return answer


    # answer = 0
    # for bag in bags:
    #     if len(bag): # 가방이 있다면,
    #         chk = 1
    #         # 가방 안에 더 작은 번호들이 담겨있는지 전부 확인
    #         for i in range(1, len(bag)):
    #             if type(bag[i]) == list:
    #                 tmplst = []
    #                 tmplst.append()
    #                 if max(bag[i]) > bag[0]:
    #                     chk = 0
    #             else:
    #                 if bag[i] > bag[0]:
    #                     chk = 0
    #         answer += chk
    #
    # return answer

n = 4
actions = ["PUT 3 INSIDE 2","SWAP 4 WITH 2","PUT 2 INSIDE 4","SET 1 LOOSE"]
print(solution(n, actions))


# n = 3
# actions = ["PUT 1 INSIDE 2","PUT 3 INSIDE 1"]
# print(solution(n, actions))

# n = 2
# actions = ["PUT 1 INSIDE 2","SET 2 LOOSE"]
# print(solution(n, actions))

# n = 2
# actions = ["PUT 1 INSIDE 2"]
# print(solution(n, actions))



# def solution(n, actions):
#
#     # 각 가방 번호를 인덱스로, 만약 가방에 뭔가 담겨있다면
#     # 그 내용물을 해당 인덱스 뒤에 리스트로 담고 있는 리스트
#     bags = [[]]+[[i+1] for i in range(n)]
#
#     for action in actions:
#         if chkact(action)[0] % 2 == 0:
#             chk, x, y = chkact(action)
#         else:
#             chk, x = chkact(action)[0], chkact(action)[1]
#
#         if chk == 0 and len(bags[x]) and len(bags[y])\
#                 and bags[x][0] == x and bags[y][0] == y:
#             bagstoputin = bags[x].copy()
#             bags[y].append(bagstoputin)
#             bags[x].clear()
#         elif chk == 1 and bags[x][0] == x:
#             while len(bags[x]) > 1:
#                 bagtoback = bags[x][-1].copy()
#                 togoidx = bagtoback[0]
#                 bags[togoidx] = bags[x].pop(-1)
#         elif chk == 2 and len(bags[x]) and len(bags[y])\
#                 and bags[x][0] == x and bags[y][0] == y:
#             bagstoswap = []
#             while len(bags[y]) > 1:
#                 bagstoswap.append(bags[y].pop(-1))
#             while len(bags[x]) > 1:
#                 bags[x].append(bags[y].pop(-1))
#             while len(bagstoswap):
#                 bags[y].append(bagstoswap.pop(-1))
#
#             # bagtoswap = bags[x][1:].copy()
#             # bags[x][1:].extend(bags[y][1:])
#             # bags[y][1:] = bagtoswap
#
#         else:  # action이 틀리거나 유효하지 않다면 -1 반환
#             return -1