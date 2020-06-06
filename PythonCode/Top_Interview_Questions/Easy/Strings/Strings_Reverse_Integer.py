from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        Args:
            s (List[str]): [description]
        """
        numStr = [digit for digit in str(x) if digit != '-']
        numStr.reverse()

        if x < 0:
            s = int(''.join(numStr))*-1
        else:
            s = int(''.join(numStr))

        if s < -1*2**31 or s > 2**31 - 1:
            return 0

        return s


def main():
    s = Solution()
    x = 1534236469
    ans = s.reverse(x)
    print(ans)


if __name__ == '__main__':
    main()
