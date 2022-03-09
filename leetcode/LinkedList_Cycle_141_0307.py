# -*- coding: utf-8 -*-
# position是表明哪个点和尾部相连的
#
# Definition for singly_linked list


# class ListNode(object):
#     def__init__(self,x):
#         self.value = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        '''
        type head :listNode
        rtype:bool
        '''
        fast, slow = head, head
        # while no fast and fast.next: no cycle，某个fast.next = None了，就是一条直线
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
