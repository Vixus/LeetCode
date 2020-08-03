class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        Note: For the purpose of this problem, we define empty string as valid palindrome.

        Example 1:

        Input: "A man, a plan, a canal: Panama"
        Output: true
        Example 2:

        Input: "race a car"
        Output: false


        Constraints:

        s consists only of printable ASCII characters.

        Args:
            s (str): [description]

        Returns:
            bool: [description]
        """
        s = [x.lower() for x in s if x.isalnum()]
        N = len(s)
        for i in range(N//2):
            if s[i] != s[-(i+1)]:
                return False

        return True


def main():
    s = Solution()
    wordstr = 'A man, a plan, a canal: Panama'
    ans = s.isPalindrome(wordstr)
    print(ans)


if __name__ == '__main__':
    main()
