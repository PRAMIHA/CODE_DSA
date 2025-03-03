#FACTORIAL IN GFG
class Solution:
    def factorial (self, n):
        # code here for factorial
        res=1
        while n>0:
            res=res*n
            n=n-1
        return res
