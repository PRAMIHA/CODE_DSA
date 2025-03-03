
#https://www.geeksforgeeks.org/problems/corner-digits1317/1----->CORNER DIGIT SUM
class Solution:
	def corner_digitSum(self, n):
		# Code here
		ld=n%10
		if n<10:
		    return n
		
		while n>0:
		    fd=n%10
		    n=n//10
		        
		return(fd+ld)
