def solution(n, words):
    answer = []
    cnt = 1

    tmp_words = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in tmp_words and words[i][0] == tmp_words[-1][-1]:
            tmp_words.append(words[i])
        else:
            return [cnt%n+1, cnt//n+1]
        cnt += 1

    return [0,0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# n = 5
# words =	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

# n = 2
# words =	["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n,words))