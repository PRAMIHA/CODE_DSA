#https://www.geeksforgeeks.org/problems/middle-of-three2926/1
class Solution:
    def middle(self, a, b, c):
        #code here
        return (a + b + c) - min(a, b, c) - max(a, b, c)

