"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        countDict = Counter(s)
        longestCount = 0
        isOdd = False
        for _, count in countDict.items():
            if count % 2 == 0:
                longestCount += count
            else:
                longestCount += count-1
                isOdd = True

        return int(longestCount+int(isOdd))


def main():
    s = Solution()
    inputStr = 'aaabbbccccddddd'
    ans = s.longestPalindrome(inputStr)
    print(ans)


if __name__ == '__main__':
    main()
