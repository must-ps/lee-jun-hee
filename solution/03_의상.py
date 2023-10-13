from collections import defaultdict

def solution(clothes):
    number_of_clothes, answer = defaultdict(int), 1
    for _, kind in clothes:
        number_of_clothes[kind] += 1
    for val in number_of_clothes.values():
        answer *= val + 1
    return answer - 1

my_list = [[1], [2, 3], [43, 5, 3]]
my_list[0]

my_dict = { 'key' : [1]}
my_dict['key']