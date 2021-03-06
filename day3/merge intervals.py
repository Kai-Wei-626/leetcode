'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings. For example, Given [[0, 30],[5, 10],[15, 20]], return false.
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return intervals
        intervals = sorted(intervals, key = lambda interval: (interval.start, interval.end))
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if  merged[-1].end >= intervals[i].start:
                merged[-1].end = max(intervals[i].end, merged[-1].end)
                
            else:
                merged.append(intervals[i])
        return merged
        
        
