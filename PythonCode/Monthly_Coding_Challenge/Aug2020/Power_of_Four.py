import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

        Example 1:

        Input: 16
        Output: true
        Example 2:

        Input: 5
        Output: false
        Follow up: Could you solve it without loops/recursion?

        Args:
            num (int): [description]

        Returns:
            bool: [description]
        """
        # if bin(num).count('1') != 1 or num < 0:
        #     return False

        # return int(math.log(num, 2)) % 2 == 0

        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num


def main():
    s = Solution()
    num = 5
    ans = s.isPowerOfFour(num)
    print(ans)


if __name__ == '__main__':
    main()
