# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        cur=head

        while cur!=None:
            lst.append(cur.val)
            cur=cur.next 

        if len(lst)%2==0:
            idx=(len(lst)+1)//2
            lst=lst[:idx]+lst[idx+1:]
        else:
            idx=len(lst)//2
            lst=lst[:idx]+lst[idx+1:]

        dummy=ListNode(0)
        tail=dummy
        for val in lst:
            tail.next=ListNode(val)
            tail=tail.next
        return dummy.next


        