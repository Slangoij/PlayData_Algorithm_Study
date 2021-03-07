# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, text):
        max_len = 0  # text요소의 길이중 최대값
        for tex in text:
            max_len = max(max_len, len(tex))

        answer = []
        for tex in text:
            if len(tex) < max_len:
                tmpstr = ' ' * (max_len - len(tex))
                answer.append(tmpstr + tex)
            else:
                answer.append(tex)

        return answer