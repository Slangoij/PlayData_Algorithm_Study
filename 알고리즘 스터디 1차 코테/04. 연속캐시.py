class Solution:
    def solution(self, n, k, addresses):
        answer = 0
        # -2, -1, 0, 1, 2, 3, 4 ,5 ,6
        # 0, 1, 2, 3, 4 -> 0, 4, 5,6,7,8,9
        now_bitrange = [0, k - 1]

        # 어드레스의 모든 요소 조회
        for i in addresses:

            # 현재 갖고 있는 바이트 범위를 벗어날 때
            if i > now_bitrange[1]:

                if i > now_bitrange[1] + k:
                    answer += k
                else:
                    answer += i - now_bitrange[1]
                now_bitrange[0] += i - now_bitrange[1]
                now_bitrange[1] = i

            elif i < now_bitrange[0]:

                if i < now_bitrange[0] - k:
                    answer += k
                else:
                    answer += now_bitrange[0] - i
                now_bitrange[1] -= now_bitrange[0] - i
                now_bitrange[0] = i

        return answer