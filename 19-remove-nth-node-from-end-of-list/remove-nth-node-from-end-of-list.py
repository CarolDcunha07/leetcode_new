# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst=[]
        c=0
        cur=head
        while cur:
            lst.append(cur.val)
            cur=cur.next
        delpos=len(lst)-n
        print(delpos)
        lst=lst[:delpos]+lst[delpos+1:]
        dummy=ListNode(0)
        tail=dummy
        for val in lst:
            tail.next=ListNode(val)
            tail=tail.next
        return dummy.next
        