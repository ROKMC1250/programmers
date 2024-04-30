def solution(s):
    s = list(map(str,s))
    answer = 0
    L = len(s)
    DP = [[0] * (L+1) for _ in range(L+1)]
    for j in range(1, L+1):
        DP[j][j] = 1
        for i in range(j-1, 0,-1):
            if j-i == 1:
                if s[i-1] == s[j-1]:
                    DP[i][j] = 2
            else:
                if s[i-1] == s[j-1] and DP[i+1][j-1] >= 1:
                    DP[i][j] = j - i + 1
    max_lst = []
    for i in range(1, L+1):
        max_lst.append(max(DP[i]))
    answer = max(max_lst)
#  a b c d c b a
#a 1 0 0 0 0 0
#b   1 0 0 0 0
#c     1 0 1 0
#d       1 0 0 0
#c         1 0 0
#b           1 0
#a             1

    return answer