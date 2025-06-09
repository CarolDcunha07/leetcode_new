class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start=str(bin(start)[2:])
        goal=str(bin(goal)[2:])
        c=0

        if len(start)<len(goal):
            start=start.zfill(len(goal))
        elif len(start)>len(goal):
            goal=goal.zfill(len(start))

        for i in range(len(start)):
            if start[i]!=goal[i]:
                c+=1
        return c

        