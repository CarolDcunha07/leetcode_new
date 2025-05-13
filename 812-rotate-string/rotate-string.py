class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new_s=goal+goal

        if len(goal)<len(s) or len(goal)>len(s):
            return False

        if s in new_s:
            return True
        else:
            return False
        