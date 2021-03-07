# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, code, message):
        answer = ''

        # 메시지가 숫자라면 문자로
        if message.isdigit():
            for i in range(int(len(message) / 2)):
                nowidx = int(message[2 * i:2 * i + 2])
                answer += code[nowidx - 1]

        # 문자라면 숫자로
        else:
            for i in message:
                tmpstr = ''
                tmpidx = code.find(i) + 1
                if tmpidx <= 9:
                    tmpstr = '0'
                tmpstr += str(tmpidx)
                answer += tmpstr

        return answer