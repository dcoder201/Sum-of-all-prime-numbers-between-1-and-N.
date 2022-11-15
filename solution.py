#User function Template for python3
import math
class Solution:
	def prime_Sum(self, n):
		# Code here
		def isprime(m):
		    if m==2:
		        return True
		    for i in range(2,int(math.sqrt(m))+1):
		        if m%i==0:
		            return False
		    else:
		        return True
		        
		s = 0
		if n == 0 or n==1:
		    return 0
		else:
    		for i in range(2,n+1):
    		    if isprime(i):
    		        s += i
		    return s
		# Code here
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends
