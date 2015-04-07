class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):

        v1 = str(version1).split('.')
        v2 = str(version2).split('.')

        l1 = len(v1)
        l2 = len(v2)

        p1 = 0
        p2 = 0


        while p1<l1 or p2<l2:

            n1 = 0
            if p1<l1:
                n1 = int(v1[p1])
            n2 = 0
            if p2<l2:
                n2 = int(v2[p2])

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            else:
                p1 +=1
                p2 +=1

        return 0