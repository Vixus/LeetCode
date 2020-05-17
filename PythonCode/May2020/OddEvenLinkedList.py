from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
        You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

        Arguments:
            head {ListNode} -- [description]

        Returns:
            ListNode -- [description]
        """
        if not head:
            return None
        elif not head.next:
            return head
        elif not head.next.next:
            return head

        oddEndPtr = head
        evenEndPtr = evenHeadPtr = head.next
        tempPtr = head.next.next

        odd = True
        while tempPtr:
            if odd == True:
                oddEndPtr.next = tempPtr
                oddEndPtr = tempPtr
                tempPtr = tempPtr.next
                oddEndPtr.next = evenHeadPtr
                odd = False
            else:
                evenEndPtr.next = tempPtr
                evenEndPtr = tempPtr
                tempPtr = tempPtr.next
                odd = True

        evenEndPtr.next = None
        return head


def main():
    head = ListNode(1)
    endPtr = head
    inputArr = [1]
    for i in range(2, 6):
        inputArr.append(i)
        node = ListNode(i)
        endPtr.next = node
        endPtr = node
    print(inputArr)

    s = Solution()
    ans = s.oddEvenList(head)
    outputArr = []
    for i in range(5):
        outputArr.append(ans.val)
        ans = ans.next

    print(outputArr)


if __name__ == '__main__':
    main()
