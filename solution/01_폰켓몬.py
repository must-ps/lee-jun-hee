def solution(nums):
    kind = len(set(nums))
    pick = len(nums) // 2
    return min(kind, pick)