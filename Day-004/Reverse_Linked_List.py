 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def reverseList(self, head):
        prev, cur = None, head
        while cur :
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev 
