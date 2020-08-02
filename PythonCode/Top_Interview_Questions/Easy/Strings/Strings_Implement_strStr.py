from typing import List
from collections import defaultdict
from collections import Counter
import sys
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implement strStr().
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Args:
            haystack (str): [description]
            needle (str): [description]

        Returns:
            int: [description]
        """
        N = len(needle)
        if N == 0:
            return 0

        for i in range(len(haystack)-N+1):
            if haystack[i:i+N] == needle:
                return i

        return -1


def main():
    s = Solution()
    haystack = "hello"
    needle = "ll"
    ans = s.strStr(haystack, needle)
    print(ans)


if __name__ == '__main__':
    main()
