# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):

        l = len(intervals)

        if l > 1:
            intervals.sort(self.comp)
            i = 1
            rt = [intervals[0]]
            r = 0
            while i < l:

                if  intervals[i].start <= rt[r].end \
                        or intervals[i].start < rt[r].start:
                    if rt[r].end < intervals[i].end:
                        rt[r].end = intervals[i].end
                    if intervals[i].start < rt[r].start:
                        rt[r].start = intervals[i].start
                else:
                    rt.append(intervals[i])
                    r += 1

                i += 1
        else:
            rt = intervals

        return rt

    def comp(self, int1, int2):
        i = int1.start - int2.start
        if i >0 :
            return 1
        elif i <0:
            return -1
        else:
            return 0

#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

    @staticmethod
    def output(lst):
        l = len(lst)

        print '[',
        for i in range(l):
            print '[', lst[i].start, lst[i].end, ']',
        print ']'

    @staticmethod
    def create(lst):
        r = []
        l = len(lst)
        for i in range(l):
            r.append(Interval(lst[i][0], lst[i][1]))
        return r

s = Solution()
Interval.output( s.merge(Interval.create([[1,3],[2,6],[8,10],[15,18]])) )
Interval.output( s.merge(Interval.create([[1,4],[0,4]])))
Interval.output( s.merge(Interval.create([[1,4],[0,0]])))
