class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        for i in range(0,len(s)):
            if s[i] in ['(','[','{']:
                stck.append(s[i])
            else :
                if len(stck)>0:
                
                    top = stck[-1]
                    if s[i] == ')' and top=='(':
                        stck.pop()
                    elif s[i] == ']' and top=='[':
                        stck.pop()
                    elif s[i] == '}' and top=='{':
                        stck.pop()
                    else:
                        return False
                else :
                    return False
        if len(stck)<=0:
            return True
        return False

                    
        