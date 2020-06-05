from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
        You may assume the integer does not contain any leading zero, except the number 0 itself.

        Args:
            digits (List[int]): [description]

        Returns:
            List[int]: [description]
        """
        num = int(''.join(map(str, digits)))

        return [int(x) for x in str(num+1)]


def main():
    s = Solution()
    digits = [1, 2, 3]
    ans = s.plusOne(digits)
    print(ans)


if __name__ == '__main__':
    main()
