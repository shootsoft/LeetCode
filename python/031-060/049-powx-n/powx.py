import math

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):

        if n==0:
            return 1
        elif x==1.0:
            return x
        elif x==-1.0:
            if n<0:
                n*=-1
            if n % 2 ==0:
                return 1.0
            else:
                return x
        y = 1
        while n!=0:
            if n>=1:
                y *= x
                n -= 1
            elif n<=-1:
                y *= 1.0/x
                n += 1
            if y == 0.0 :
                return y
        return y

class Solution1:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if(n==0):
            return 1;
        elif(n==1):
            return x;
        if(n<0):
            return self.pow(1/x,-n);
        else:
            if(n%2==0):
                return self.pow(x*x,n/2);
            else:
                return self.pow(x*x,(n-1)/2)*x;

s = Solution()

print s.pow(-1.00000, -2147483648)

print s.pow(2, 0)
print s.pow(2, 1)
print s.pow(2, 2)
print s.pow(2, 3)
print s.pow(2, 3)
print s.pow(2, -3)
print s.pow(1.00001, 123456)

print math.pow(-1.00000, -2147483648)
print s.pow(0.00001, 2147483647)
