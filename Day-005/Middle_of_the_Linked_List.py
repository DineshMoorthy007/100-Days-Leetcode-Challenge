class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def middleNode(self, head):
        s = f = head

        while f and f.next :
            s = s.next 
            f = f.next.next

        return s
