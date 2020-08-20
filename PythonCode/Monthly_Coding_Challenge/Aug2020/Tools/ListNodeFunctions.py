import numpy as np

# Definition for a binary tree node.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def ArrToListNode(nodeValArr):
    if len(nodeValArr) == 0:
        return ListNode(None)

    head = ListNode(nodeValArr[0])
    currNode = head

    for val in nodeValArr[1:]:
        currNode.next = ListNode(val)
        currNode = currNode.next

    return head


def ListNodeToArr(head):
    currNode = head
    listNodeArr = []

    while currNode:
        listNodeArr.append(currNode.val)
        currNode = currNode.next

    return listNodeArr
