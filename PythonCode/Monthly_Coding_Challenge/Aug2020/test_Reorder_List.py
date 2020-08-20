from Tools.ListNodeFunctions import ListNodeToArr, ArrToListNode
from Reorder_List import Solution


def test1():
    s = Solution()
    head = ArrToListNode([1, 2, 3, 4])
    s.reorderList(head)
    ans = ListNodeToArr(head)
    assert ans == [1, 4, 2, 3]


def test2():
    s = Solution()
    head = ArrToListNode([1, 2, 3, 4, 5])
    s.reorderList(head)
    ans = ListNodeToArr(head)
    assert ans == [1, 5, 2, 4, 3]
