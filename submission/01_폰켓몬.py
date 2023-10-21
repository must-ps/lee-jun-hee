def solution(nums):
    pick_num = len(nums)//2
    unique_element_num = len(set(nums))
    answer = min(unique_element_num, pick_num)
    return answer