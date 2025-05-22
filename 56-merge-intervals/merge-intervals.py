class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lst=[]
        intervals.sort(key=lambda x:x[0])
        prev=intervals[0]

        for interval in intervals[1:]:
            if interval[0]<=prev[1]:
                prev[1]=max(prev[1],interval[1])
            else:
                lst.append(prev)
                prev=interval
        lst.append(prev)
        return lst

        