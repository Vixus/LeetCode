"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.
You may return the answer in any order.

Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:
1 <= N <= 9
0 <= K <= 9
"""

from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        outputArr = []

        def nextDigit(num, K, digitCount):
            numUp = num % 10 + K
            numDown = num % 10 - K

            if digitCount == 0:
                outputArr.append(num)
                return

            if numUp <= 9:
                nextDigit(num*10+numUp, K, digitCount-1)

            if numDown >= 0 and numUp != numDown:
                nextDigit(num*10+numDown, K, digitCount-1)

        if N == 1:
            return list(range(10))

        for x in range(1, 10):
            nextDigit(x, K, N-1)

        return outputArr


def main():
    s = Solution()
    N = 1
    K = 0
    ans = s.numsSameConsecDiff(N, K)
    print(ans)


if __name__ == '__main__':
    main()
