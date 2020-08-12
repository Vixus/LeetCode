"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        oldRowData = [1]
        for row in range(rowIndex+1):
            newRowData = [1]*(row+1)
            if row >= 2:
                for i in range(1, len(newRowData)-1):
                    newRowData[i] = oldRowData[i-1]+oldRowData[i]
            oldRowData = newRowData
        return newRowData


def main():
    s = Solution()
    rowIndex = 3
    ans = s.getRow(rowIndex)
    print(ans)


if __name__ == '__main__':
    main()
