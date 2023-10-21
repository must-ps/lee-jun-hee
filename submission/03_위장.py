def solution(clothes):
    my_dict = dict()
    for c in clothes:
        if c[1] in my_dict.keys():
            my_dict[c[1]].append(c[0])
        else:
            my_dict[c[1]] = [c[0]]
    answer = 1
    for key in my_dict:
        answer*=(len(my_dict[key])+1) # 아예 해당 항목을 선택하지 않을 수 있음도 경우의 수에 고려해야함
    return answer-1 # 아무것도 고르지 않은 경우는 제외해야함으로 -1을 해줌