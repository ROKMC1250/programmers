def solution(n):
    number = ['1', '2', '4']
    answer_lst = []
    while n > 3:
        remainder = n % 3
        if remainder == 0:
            answer_lst.insert(0, number[2])
            n -= 1
        else:
            answer_lst.insert(0, number[remainder-1])
        n //= 3

    answer_lst.insert(0, number[n-1])
    answer = ''.join(answer_lst)
    return answer