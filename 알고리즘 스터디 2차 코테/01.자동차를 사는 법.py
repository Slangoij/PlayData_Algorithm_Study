# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, prices):
        prices = list(set(prices))

        prices.sort()

        if len(prices) >= 3:
            return prices[2]
        else:
            return -1