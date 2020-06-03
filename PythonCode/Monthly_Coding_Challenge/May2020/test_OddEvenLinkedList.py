from OddEvenLinkedList import Solution, ListNode


def test1():
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

    assert outputArr == [1, 3, 5, 2, 4]
