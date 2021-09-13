class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        llist = []
        for i in range(1,head + 1):
            llist.append(i)
        llist.reverse()
        return llist

Solution().reverseList(5)