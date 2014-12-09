import datetime

class Solution:
    # @return a string
    def convert(self, s, nRows):

    	l = len(s)
    	if nRows==1 or nRows>=l:
    		return s
    	else :
    		dim =  l - nRows + 1
    		arr = [([''] * dim) for i in range(nRows)]
    		x = y = 0 # position
    		d = 0 # 2 direction 0 down 1 right up
    		for i in range(l):
    			arr[x][y] = s[i]
    			#print x , y
    			if(d ==0) :
    				x += 1
    				if(x>=nRows):
    					d = 1
    					x -= 2
    					y += 1
    			else:
    				x -= 1
    				y += 1
    				if(x<0) :
    					d = 0
    					x += 2
    					y -=1

    		r = ''
    		for i in range(nRows):
    			#print arr[i]
    			r += ''.join(arr[i])
    		return r

s = Solution()
r = s.convert('PAYPALISHIRING', 3)
print r
print 'PAHNAPLSIIGYIR'
print s.convert('A', 2)
print s.convert('ABC', 2)
print s.convert('ABCDE', 2)
print s.convert('PAYPALISHIRING', 8)
print s.convert('chrynqxqqmlfotpqhvokiiammqmvxjvbsoaifzyxnjcberrnmixxsyjhovengbpyqrixqgwdrygxrxkfhicainhwi', 24)

starttime = datetime.datetime.now()
print s.convert("twckwuyvbihajbmhmodminftgpdcbquupwflqfiunpuwtigfwjtgzzcfofjpydjnzqysvgmiyifrrlwpwpyvqadefmvfshsrxsltbxbziiqbvosufqpwsucyjyfbhauesgzvfdwnloojejdkzugsrksakzbrzxwudxpjaoyocpxhycrxwzrpllpwlsnkqlevjwejkfxmuwvsyopxpjmbuexfwksoywkhsqqevqtpoohpd", 4)
endtime = datetime.datetime.now()
print (endtime - starttime)

starttime = datetime.datetime.now()
print s.convert("rbgneoikagdaszofomldsoiyvqcubmbsnjhuaqeayjdrktyzhjczxkasaeodqrxgdfadvgftpkmzgkyntdptnpnqtctmvrsywudtalmpxbqdlprfsgahxnxsrtenkynistduerjdsaherallilshyqzqjgfvgufznittzfzshgyyijjqwbzwtyoeetbnqgodqjzsoymxgkvovggrkfndfckmxlznuntkwuensqkaciqxowqydgekkqwhbxxvkqijkowehiejqujhsbhxhnhrdebfbycoomxabveiditwecdwgmtnaahdgikkinyyzxycsekxoevsiaoonjenjnqsxbcfqadrzdutheqvkonvodlbmrqxejpbmticvltuonnxugsguhdkkpoygeynnpozjzdekxbbmoygwtpsasdnhrnqvldldtkmsosfntizkiigbzberetbvitswydztqlogfttbdulletpdwvxaoaxytqurvtmlgatmtopylckpxzvuuuukusinkdghystftotodinokzfhycbuwygqsofctljsgezbvsryceomdvvdyzzuxfnrwstpgejmlkpgegggnuusrswprxmqdzhzrcqzgcltmczrjfxwbuotmmkfkwvnvcopgeomgcivehmnpllsfcntoyyautpsxdhdkxsszangjbtanhtujgoxeoabkpthtcnfzhxbhlhsmctbjmwuumuzcucmjxwcbjhcqhdzsmrgpmkayivtwpuyjyl", 647)
endtime = datetime.datetime.now()
print (endtime - starttime)



