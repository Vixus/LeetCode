"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        outputArr = ['']*(n)
        for i in range(n):
            div3 = (i+1) % 3 == 0
            div5 = (i+1) % 5 == 0

            if not div3 and not div5:
                outputArr[i] = str(i+1)
            elif div3:
                outputArr[i] = 'Fizz'

            if div5:
                outputArr[i] += 'Buzz'

        return outputArr


def main():
    s = Solution()
    n = 15
    ans = s.fizzBuzz(n)
    print(ans)


if __name__ == '__main__':
    main()
