class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set={}
        for i in range(0,len(s)):
            if s[i] in s_set:
                s_set[s[i]]+=1
            else:
                s_set[s[i]]=1
        print(s_set)
        for i in range(0,len(t)):
            if t[i] in s_set:
                s_set[t[i]]-=1
            if t[i] not in s_set or s_set[t[i]]<0:
                return False
        if sum(list(s_set.values()))>0 :
           return False
        return True

        
        