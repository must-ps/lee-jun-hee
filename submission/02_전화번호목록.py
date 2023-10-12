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