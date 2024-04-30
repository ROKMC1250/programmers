def solution(n):
    answer = 0
    facto = [0] * (n+1)
    facto[0] = 1
    facto[1] = 1
    for i in range(2, n+1):
        facto[i] = facto[i-1] * i 
        
    for i, j in enumerate(range(n,-1,-1)):
        if i > j:
            break
        else:
            if (j-i) >= i:
                answer += facto[j] // (facto[i] * facto[j - i])
            else:
                answer += facto[j] // (facto[j-i] * facto[i])
    return answer % 1000000007
#1 1
#2 11 2
#3 111 12 21  
#  3C0 + 2C1
#4 1111 121 112 211 22 
#. 4C0 + 3C1 + 2C2
#5 11111 1121 1112 1211 2111 221 122 212 
#  5C0 + 4C1 + 3C2
#6 111111 11211 11121 11112 12111 21111 1122 2112 2211 1221 1212 2121 33 
#  6C0 + 5C1 + 4C2 + 3C3