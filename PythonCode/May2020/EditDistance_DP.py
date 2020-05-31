from typing import List
from collections import defaultdict
from itertools import product


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
        You have the following 3 operations permitted on a word:
        Insert a character
        Delete a character
        Replace a character

        Arguments:
            word1 {str} -- [description]
            word2 {str} -- [description]

        Returns:
            int -- [description]
        """
        word1, word2 = '!'+word1, '!'+word2
        len1, len2 = len(word1), len(word2)

        dp_matrix = defaultdict(int)

        for i1 in range(len1):
            dp_matrix[i1, 0] = i1
        for i2 in range(len2):
            dp_matrix[0, i2] = i2

        for i1, i2 in product(range(1, len1), range(1, len2)):
            if word1[i1] == word2[i2]:
                dp_matrix[i1, i2] = dp_matrix[i1-1, i2-1]
            else:
                dp_matrix[i1, i2] = 1+min(
                    dp_matrix[i1, i2-1],  # Add letter
                    dp_matrix[i1-1, i2],  # Remove letter
                    dp_matrix[i1-1, i2-1])  # Replace letter

        return dp_matrix[len1-1, len2-1]

        # word1, word2 = "!" + word1, "!" + word2
        # n_1, n_2 = len(word1), len(word2)
        # dp = [[0] * n_2 for _ in range(n_1)] # THIS IS VERY NICE!!!!!!

        # for i_1 in range(n_1): dp[i_1][0] = i_1
        # for i_2 in range(n_2): dp[0][i_2] = i_2

        # for i_1 in range(1, n_1):
        #     for i_2 in range(1,n_2):
        #         Cost = (word1[i_1] != word2[i_2])
        #         dp[i_1][i_2] = min(dp[i_1-1][i_2] + 1, dp[i_1][i_2-1] + 1, dp[i_1-1][i_2-1] + Cost)

        # return int(dp[-1][-1])


def main():
    s = Solution()
    word1 = 'horse'
    word2 = 'ros'
    ans = s.minDistance(word1, word2)
    print(ans)


if __name__ == '__main__':
    main()
