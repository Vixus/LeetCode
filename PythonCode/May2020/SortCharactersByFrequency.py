import numpy as np
from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Given a string, sort it in decreasing order based on the frequency of characters.

        Arguments:
            s {str} -- [description]

        Returns:
            str -- [description]
        """
        cnt = Counter(s)
        sortedStr = ''

        for letter, count in cnt.most_common():
            for i in range(count):
                sortedStr += letter

        return sortedStr


def main():
    s = Solution()
    ans = s.frequencySort('tree')
    print(ans)


if __name__ == '__main__':
    main()
