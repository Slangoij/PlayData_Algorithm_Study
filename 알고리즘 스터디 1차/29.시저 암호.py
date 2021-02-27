def push_chr(cha, n):
    if cha==' ':
        return ' '
    else:
        cha_int=ord(cha)+n
        if cha.islower() and cha_int>ord('z'):
            cha_int=cha_int-ord('z')+ord('a')-1
        elif cha.isupper() and cha_int>ord('Z'):
            cha_int=cha_int-ord('Z')+ord('A')-1
        return chr(cha_int)

def solution(s, n):
    answer = ''
    leng = len(s)
    for i in range(0,leng):
        answer+=push_chr(s[i],n)
    return answer