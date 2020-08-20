"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

from Tools.ListNodeFunctions import ListNodeToArr, ArrToListNode
from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None

        # Interweave lists
        head1, head2 = head, prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp

        ##### THIS SOLUTION IS TOO SLOW #####
        # # Find tail node
        # currNode = head
        # while currNode:
        #     if currNode.next:
        #         currNode = currNode.next
        #     else:
        #         reverseNode = currNode
        #         break

        # currNode = head
        # tempNode = head
        # while currNode.next != reverseNode and reverseNode.next != currNode:
        #     if tempNode.next != reverseNode:
        #         tempNode = tempNode.next
        #     else:
        #         tempNode.next.next = currNode.next
        #         currNode.next = tempNode.next
        #         currNode = currNode.next.next
        #         reverseNode = tempNode

        # if currNode.next == reverseNode:
        #     reverseNode.next = None
        # else:
        #     currNode.next = None


def main():
    s = Solution()
    head = ArrToListNode([])
    s.reorderList(head)
    print(ListNodeToArr(head))


if __name__ == '__main__':
    main()
