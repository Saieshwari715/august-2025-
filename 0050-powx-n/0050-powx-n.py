class Solution:
    def myPow(self, x: float, n: int) -> float:
        p=1
        if(n<0):
            x=1/x
            n=-n
        while n>0:
            if(n%2==1):
                p*=x
            x*=x
            n//=2
        return p