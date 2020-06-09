from typing import List
from collections import defaultdict
from collections import Counter
import sys
import re


class Solution:
    def myAtoi(self, str: str) -> int:
        """
        Implement atoi which converts a string to an integer.
        The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
        The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
        The first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
        If no valid conversion could be performed, a zero value is returned.

        Note:
        Only the space character ' ' is considered as whitespace character.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

        Args:
            str (str): [description]

        Returns:
            int: [description]
        """
        if len(str) == 0:
            return 0

        x = str.split()
        if not x:
            return 0
        x = re.search('[+-]?[0-9]+', x[0])

        if not x or x.start() != 0:
            return 0

        try:
            num = int(x.group(0))
        except:
            return 0

        if num > 0:
            num = min(num, 2**31-1)
        else:
            num = max(num, -2**31)

        return num


def main():
    s = Solution()
    sStr = ' '
    ans = s.myAtoi(sStr)
    print(ans)


if __name__ == '__main__':
    main()
