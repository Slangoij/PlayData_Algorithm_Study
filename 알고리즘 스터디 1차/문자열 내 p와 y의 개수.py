def solution(s):
    p_cnt=s.count('p')+s.count('P')
    if p_cnt:
        y_cnt=s.count('y')+s.count('Y')
        if p_cnt==y_cnt:
            return True
        else:
            return False
    else:
        return False