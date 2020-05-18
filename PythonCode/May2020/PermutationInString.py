from typing import List
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

        Arguments:
            s1 {str} -- [description]
            s2 {str} -- [description]

        Returns:
            bool -- [description]
        """
        # cnt_s1 = Counter(s1)
        # s1_length = len(s1)
        # s2_length = len(s2)

        # if s2_length < s1_length:
        #     return False

        # i = 0
        # while i <= s2_length-s1_length:
        #     subset_s2 = s2[i:s1_length+i]
        #     cnt_s2 = Counter(subset_s2)
        #     if cnt_s1 == cnt_s2:
        #         return True
        #     i += 1

        # return False

        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        s1_hash = sum(hash(ch) for ch in s1)
        s2_hash = sum(hash(s2[k]) for k in range(len_s1))

        if s1_hash == s2_hash:
            return True

        for k in range(len_s1, len_s2):
            s2_hash += hash(s2[k]) - hash(s2[k - len_s1])
            if s1_hash == s2_hash:
                return True
        return False


def main():
    s = Solution()
    ans = s.checkInclusion('ab', 'eidbaooo')
    print(ans)


if __name__ == '__main__':
    main()
