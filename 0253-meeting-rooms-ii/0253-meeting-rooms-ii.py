class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        groups = [[intervals[0][0], intervals[0][1]]]
        
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            newGrp = True
            for j in range(len(groups)):
                gs = groups[j][0]
                ge = groups[j][1]
                if s >= ge:
                    groups[j][1] = e
                    newGrp = False
                    break
            if newGrp:
                groups.append(intervals[i])

        print(intervals)
        print(groups)
        return(len(groups))

        
