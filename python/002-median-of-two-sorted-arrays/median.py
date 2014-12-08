class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        
        i = 0
        j = 0

        la = len(A)
        lb = len(B)

        while(lb>0 and j<lb):
        	#print la, lb, i,j, A
        	if(la==0):
        		A.insert(0,B[j])
        		j+=1
        		la+=1
        	elif(A[i]>=B[j]):
        		#print i, A
        		A.insert(i, B[j])
        		i +=1
        		j +=1
        		la+=1
        	elif(i==la-1):
        		A.append(B[j])
        		i +=1
        		j +=1
        		la+=1
        	else:
        		i +=1

        l = la
        if(l==0):
        	return 0
        elif(l==1):
        	return A[0]
        elif(l%2==0):
        	#print l/2,l/2-1, A
        	return (A[l/2]+A[l/2-1])/2.0
        else:
        	return A[l/2]

s = Solution()
print s.findMedianSortedArrays([], [1])
print s.findMedianSortedArrays([1,1], [1,2])
print s.findMedianSortedArrays([1,5,6,7,10], [2,3,4,8,9])
print s.findMedianSortedArrays([2], [])
print s.findMedianSortedArrays([], [1,2,3,4])