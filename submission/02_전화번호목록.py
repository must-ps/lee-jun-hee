'''
시간초과 난 O(n^2)짜리 풀이

def solution(phone_book):
    for i in range(0,len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if (len(phone_book[i])!=len(phone_book[j])):
                longer = max(phone_book[i], phone_book[j],key=len)
                shorter = min(phone_book[i], phone_book[j],key=len)
                if (shorter == longer[:len(shorter)]):
                    return False
    return True

'''

# 재시도해서 O(n)으로 품

def solution(phone_book):
    phone_book.sort()
    for i in range(0,len(phone_book)-1):
        left = phone_book[i]
        right = phone_book[i+1]
        if (len(left)<len(right)):
            if (left == right[:len(left)]):
                return False                
    return True