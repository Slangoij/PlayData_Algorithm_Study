from itertools import combinations

def wth_aftsplit(words, font, lines):
    min_width = 10001
    for combi in combinations(list(range(1,len(words))), lines-1):
        wordlst = []
        idx = 0
        for i in combi:
            wordlst.append(words[idx:i])
            idx = i
        wordlst.append(words[idx:])
    
        ret = 0
        for word in wordlst:
            tmplen = 0
            if len(word)>1:
                for wrd in word:
                    tmplen += len(wrd)*(font+2)
                tmplen += (len(word)-1)*(font+2)
            else:
                tmplen += len(word[0])*(font+2)
            ret = max(ret, tmplen)
        min_width = min(min_width, ret)
    
    return ret
    

def solution(text, width, height):
    words = text.split(' ')

    ans = -1
    for lines in range(1, len(words)+1):
        if wth_aftsplit(words, 7, lines) >= 10001:
            continue
        for font in range(height//2//lines, 6, -1):
            if wth_aftsplit(words, font, lines) <= width:
                ans = max(ans, font)

    if ans >= -1:
        return ans
    return -1

# text = "ONE TWO THREE FOUR FIVE"
# width = 150
# height = 10000
text = "ONE TWO THREE FOUR FIVE"
width = 150
height = 40
print(solution(text, width, height))





    # for i in range(1<<(len(words)-1)):
    #     tmp_width, idx = 0, 0
    #     tmp_height = font*2
    #     for j in range(len(words)-1):
    #         if i&(1<<j):
    #             if idx+1 < j:
    #                 tmp_width = max(len(words[idx:j]+1)*(font+2), tmp_width)
    #             else:
    #                 tmp_width = max(len(words[idx:j]), tmp_width)
    #             tmp_height += font*2
    #             # tmp_area.append(words[idx:j])
    #             idx = j
    #     # tmp_area.append(words[idx:])
    #     list.append(abs(width-tmp_width)+abs(height-tmp_height), tmp_width, tmp_height)

    # list.sort(key=lambda x: x[0])
    # return list[0][1:]