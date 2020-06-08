from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t , write a function to determine if t is an anagram of s.

        Args:
            s (str): [description]
            t (str): [description]

        Returns:
            bool: [description]
        """
        sCount = Counter(s)
        tCount = Counter(t)

        return sCount == tCount


def main():
    s = Solution()
    sStr = 'anagram'
    tStr = 'nagaram'
    ans = s.isAnagram(sStr, tStr)
    print(ans)


if __name__ == '__main__':
    main()
