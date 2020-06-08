from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        Note: For the purpose of this problem, we define empty string as valid palindrome.

        Args:
            s (str): [description]

        Returns:
            bool: [description]
        """
        s = [x.lower() for x in s if x.isalnum()]
        N = len(s)
        for i in range(N//2):
            if s[i] != s[N-1-i]:
                return False

        return True


def main():
    s = Solution()
    sStr = '0P'
    ans = s.isPalindrome(sStr)
    print(ans)


if __name__ == '__main__':
    main()
