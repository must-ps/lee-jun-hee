# 첫번쨰 - 잘못된 풀이 - 테스트케이스 몇개 통과 못함

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

# 다시 고쳐서 통과된 풀이

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