def solution(genres, plays):
    answer = []
    gen = list(set(genres))

    alll = [[] for _ in range(len(gen))]
    for idx, i in enumerate(zip(genres, plays)):
        # 여기서 gen 기껏 다 만들어놓고 genres에 append 해 인덱스에러로 시간 낭비!!!!!!
        alll[gen.index(i[0])].append((idx, i[1]))

    new = []
    # alll = [[[0, 500], [2, 150], [3, 800]], [[1, 600], [4, 2500]]]
    for i in alll:
        # print(i)
        sum1 = 0
        for j in i:
            sum1 += j[1]
        k = sorted(i, key=lambda x: -x[1])
        k.append(sum1)
        new.append(k)

    # print(alll)
    new = sorted(new, key=lambda x: x[-1], reverse=True)
    # print(new)

    for i in new:
        answer.append(i[0][0])
        if len(i) > 2:
            answer.append(i[1][0])

    return answer


# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 600, 150, 800, 2500]

# genres = ['classic', 'pop', 'bbong', 'blues', 'kpop']
# plays = [500, 600, 150, 800, 2500]

# genres = ['classic']
# plays = [500]

genres = ['pop', 'pop', 'pop', 'rap', 'rap']
plays = [45,50,40, 60, 70]

print(solution(genres,plays))