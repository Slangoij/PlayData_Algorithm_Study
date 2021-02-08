def solution(participant, completion):
    answer = ''

    leng_p = len(participant)
    participant.sort()
    completion.sort()

    i = 0
    while i < leng_p - 1:
        if participant[i] == completion[i]:
            i += 1
        else:
            answer = participant[i]
            break

    if answer == '':
        answer = participant[-1]

    #     for comple in completion:
    #         participant.remove(comple)

    #     answer=participant[0]

    return answer