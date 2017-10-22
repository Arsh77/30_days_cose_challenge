    def removeDuplicates(self,head):
        #Write your code here
        cur = head
        while cur is not None and cur.next is not None:
            while cur.next is not None and cur.data is cur.next.data:
                cur.next = cur.next.next
            cur = cur.next
        return head