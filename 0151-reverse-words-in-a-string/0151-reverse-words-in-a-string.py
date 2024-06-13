class Solution:
    def reverseWords(self, s: str) -> str:
        stck=[]
        stck = s.split()
        new_s=''
        for i in range(0,len(stck)-1):
            new_s+=stck.pop()+' '
        new_s+=stck.pop()
        return new_s