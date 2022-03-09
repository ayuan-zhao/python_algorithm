class Solution:
    #recursion
    def reverseList(self,head):
        def reverse(pre,cur):
            if not cur:
                return pre
            tmp = cur.next
            cur.next = pre
            return reverse(cur,tmp)
        return reverse(None,head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList1(self,head):
        curr = head
        prev = None
        while curr:
            # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            temp = curr.next
            #反转
            curr.next = prev
            #更新pre、cur指针
            prev = curr
            curr= temp
            #prev is the new head,curr now is None
            
        return prev    
    #time: o(n)
    #spaceo(1)
        