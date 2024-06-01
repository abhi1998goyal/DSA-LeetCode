class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            x = 1 / x
            n = -n
            return self.myPow(x,n)
        else :
            if n%2==1:
                y=self.myPow(x,(n-1)//2)
                return y*y*x
            else :
                y=self.myPow(x,(n)//2)
                return y*y