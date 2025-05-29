# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst=[]
        cur=head

        while cur: 
            lst.append(cur.val)
            cur=cur.next

        num=''.join(str(x) for x in lst)
        print(num)
        if num==num[::-1]:
            return True 
        else:
            return False
        