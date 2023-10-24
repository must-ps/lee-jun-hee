def solution(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(p)
        elif stack:
            stack.pop()
        else:
            return False
    return not stack

    # cnt = 0
    # for p in s:
    #     if p == "(":
    #         cnt += 1
    #     elif cnt > 0:
    #         cnt -= 1
    #     else:
    #         return False
    # return cnt == 0
    