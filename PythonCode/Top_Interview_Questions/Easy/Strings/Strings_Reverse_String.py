from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Write a function that reverses a string. The input string is given as an array of characters char[].
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        You may assume all the characters consist of printable ascii characters.

        Args:
            s (List[str]): [description]

        Returns:
            [type]: [description]
        """
        # s.reverse()

        N = len(s)
        for i in range(N//2):
            s[i], s[N-i-1] = s[N-i-1], s[i]

        return


def main():
    s = Solution()
    input = ["h", "e", "l", "l", "o"]
    s.reverseString(input)
    print(input)


if __name__ == '__main__':
    main()
