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

# # 문제 해설
# def solution(n, actions):
#     # 가방이 어디에 놓여있는지 나타내기 위한 리스트 선언
#     # 각 인덱스는 가방의 번호를, 원소는 해당 가방이 놓여있는 가방의 번호를 나타냄 
#     # ex) ground[1] = 2 : 1번 가방이 2번 가방 안에 놓여있음 
#     # 0: 땅에 놓여있음을 의미 
#     # 인덱스와 가방번호를 맞춰주기 위해 n+1 길이의 리스트로 생성 
#     ground = [0] * (n+1)

#     for action in actions:
#         action = action.split(' ') # 공백을 기준으로 action 문자열 분리 
#         if action[0] == 'PUT':
#             i, j = int(action[1]), int(action[3])
#             if (ground[i] | ground[j]) == 0: # 두 가방은 반드시 땅에 놓여있어야 함
#                 ground[i] = j # i가 j안에 놓여있음을 마킹 
#             else:
#                 return -1
#         elif action[0] == 'SET' :
#             i = int(action[1])
#             if ground[i] == 0: # 가방 i는 반드시 바닥에 놓여있어야 함 
#                 # ground 리스트를 순회하며 가방이 i안에 있다면
#                 # 바닥에 놓음(0으로 마킹)
#                 for j in range(1, n+1):
#                     if ground[j] == i: 
#                         ground[j] = 0 
#             else:
#                 return -1
#         elif action[0] == 'SWAP':
#             i, j = int(action[1]), int(action[3])
#             if (ground[i] | ground[j]) == 0: # 두 가방은 반드시 땅에 놓여있어야 함
#                 # ground 리스트를 순회하며 
#                 # i안에 있는 가방과 j안에 있는 가방을 바꿔줌 
#                 for c in range(1, n+1):
#                     if ground[c] == i:
#                         ground[c] = j
#                     elif ground[c] == j:
#                         ground[c] = i
#             else:
#                 return -1


#     # 완성된 ground 리스트에 대해
#     # 바닥에 놓여진 가방의 개수를 카운트해준다
#     # 만약, 가방이 자신의 가방 번호보다 더 작은 번호의 가방에 들어가있다면, 적절하지 않으므로 -1을 리턴한다 
#     ans = 0
#     for i in range(1, n+1):
#         if ground[i] == 0:
#             ans += 1
#         elif ground[i] < i:
#             return -1
#     return ans


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