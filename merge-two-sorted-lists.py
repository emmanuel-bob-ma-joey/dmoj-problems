# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        values = []
        p1 = list1
        p2 = list2
        while (p1 or p2):
            if p1 and p2:
                if p1.val < p2.val:
                    values.append(p1.val)
                    p1 = p1.next
                else:
                    values.append(p2.val)
                    p2 = p2.next
            elif p1:
                values.append(p1.val)
                p1 = p1.next
            else:
                values.append(p2.val)
                p2 = p2.next
        if values == []:
            return None
        output = ListNode(values.pop(0),None)
        head = output
        while len(values)>0:
            output.next= ListNode(values.pop(0),None)
            output = output.next
        return head
        