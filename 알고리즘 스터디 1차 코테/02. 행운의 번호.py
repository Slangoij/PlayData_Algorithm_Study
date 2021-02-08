class Solution:
    def solution(self, s):
        answer = 0

        # 체크할 부분문자열의 첫 인덱스
        for i in range(len(s)):
            [1.,52.4,6]
            # 체크할 부분문자열의 마지막 인덱스
            for j in range(i + 1, len(s)):

                # 부분 문자열의 길이가 짝수일 때 확인,
                if (j - i) % 2 == 1:
                    s_part = s[i:j + 1]  # 인덱스 i부터 j까지

                    half = int((j - i + 1) / 2)

                    lft_s = s_part[:half]  # 왼쪽 부분
                    rgt_s = s_part[half:]  # 오른쪽 부분

                    sum_l = sum_r = 0  # 각각 왼쪽 부분의 숫자합, 오른쪽부분...

                    for k in range(len(lft_s)):
                        sum_l += int(lft_s[k])
                        sum_r += int(rgt_s[k])

                    # 만약 부분 문자열이 행운의번호라면 최대값으로 정답 업데이트
                    # 두 합이 같으면 행운의 번호
                    if sum_r == sum_l:
                        answer = max(answer, (j - i + 1))

        return answer