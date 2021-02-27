def solution(answers):
    answer = []

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    solv1 = solv2 = solv3 = 0
    prob_leng = len(answers)
    supo_leng1 = len(supo1)
    supo_leng2 = len(supo2)
    supo_leng3 = len(supo3)
    for i in range(0, prob_leng):
        if answers[i % prob_leng] == supo1[i % supo_leng1]:
            solv1 += 1
        if answers[i % prob_leng] == supo2[i % supo_leng2]:
            solv2 += 1
        if answers[i % prob_leng] == supo3[i % supo_leng3]:
            solv3 += 1

    max_right_person = max(solv1, solv2, solv3)
    if solv1 == max_right_person:
        answer.append(1)
    if solv2 == max_right_person:
        answer.append(2)
    if solv3 == max_right_person:
        answer.append(3)

    if len(answer) > 1:
        answer.sort()
    return answer