def solution(phone_number):
    answer = ''
    leng=len(phone_number)
    for i in range(0,leng-4):
        answer+='*'
    for i in range(0,4):
        answer+=phone_number[leng-4+i]
    return answer