class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # sort the intervals, based on the start times. 
        intervals.sort(key = lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return(False)
        
        return(True)
        