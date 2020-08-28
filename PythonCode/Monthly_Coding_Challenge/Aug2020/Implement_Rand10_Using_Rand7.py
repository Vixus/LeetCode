"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.
Do NOT use system's Math.random().

Example 1:
Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 
Note:
rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.

Follow up:
What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
"""
from typing import List
from random import randint


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x = rand7()
        y = rand7()
        index = x+(y-1)*7
        while index > 40:
            index = self.rand10()
        return (index-1) % 10+1


def rand7():
    return randint(1, 7)


def main():
    s = Solution()
    n = 3
    ans = []
    for _ in range(n):
        ans.append(s.rand10())
    print(ans)


if __name__ == '__main__':
    main()
