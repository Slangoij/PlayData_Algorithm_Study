# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.

def chkact(action):
    actlst = action.split(' ')
    if actlst[0] == 'PUT' and actlst[2] == 'INSIDE':
        return 0, int(action[1]), int(action[3])
    elif actlst[0] == 'SET:
        return 1, int(action[1])
    elif actlst[0] == 'SWAP' and actlst[2] == 'WITH':
        return 2, int(action[1]), int(action[3])


def solution(n, actions):
    # 각 가방 번호를 인덱스로, 만약 가방에 뭔가 담겨있다면 그 내용물을 리스트로 담고 있는 리스트
    status = [[i + 1] for i in range(n + 1)]

    for action in actions:
        nowlst = chkact(action)
        if nowlst[0] == 0 and \
                status[nowlst[1]][0] == nowlst[1] and not len(status[nowlst[2]]):
            pass
        elif nowlst[0] == 1 and status[nowlst[1]][0] == nowlst[1]:
            pass
        elif nowlst[0] == 2 and \
                status[nowlst[1]][0] == nowlst[1] and not len(status[nowlst[2]]):


        else:  # action이 틀리거나 유효하지 않다면 -1 반환
            return -1

    return 0


n = 2
actions = ["PUT 1 INSIDE 2"]
print(solution(n, actions))