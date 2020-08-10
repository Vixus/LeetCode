"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        offset = ord('A')-1
        colIndex = 0
        for i, char in enumerate(s[::-1]):
            colIndex += (ord(char)-offset)*26**i
        return colIndex


def main():
    s = Solution()
    wordStr = 'ZY'
    ans = s.titleToNumber(wordStr)
    print(ans)


if __name__ == '__main__':
    main()
