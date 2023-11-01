# 첫번쨰 - 잘못된 풀이 - 테스트케이스 몇개 통과 못함 --------------------------------------

def solution(s):
    
    # edge case
    if s[0]!='(': 
        return False

    open_num = 0 
    for c in s:
        if (c=="("):
            open_num+=1
        else:
            open_num-=1
            if open_num<0: 
                return False
    return (open_num==0)



# 다시 고쳐서 통과된 풀이 -------------------------------------------------------------
# comment : 그런데 너무 엣지케이스를 여럿 고려해야하는 것 같은데 ㅠㅠ 이게 최선일까..?


def solution(s):
    
    # edge case
    if s[0]!='(': # ) 요걸로 시작하면 아예 성립 불가
        return False

    open_num = 0 
    for c in s:
        if (c=="("):
            open_num+=1
        else:
            open_num-=1
            if open_num<0: # 요부분 추가 (ex) "())("-> 요런 케이스를 생각못함..
                return False
    return (open_num==0)



# 아주 약간의 리팩토링을 진행한 최종버전 ----------------------------------------------------

def solution(s):
    
    # edge case
    if s[0]!='(': 
        return False

    open_num = 0 
    for c in s:
        if (c=="("):
            open_num+=1
        else:
            if (open_num-1<0): 
                return False
            open_num-=1
    return (open_num==0)