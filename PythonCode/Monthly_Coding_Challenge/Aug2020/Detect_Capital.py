class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Given a word, you need to judge whether the usage of capitals in it is right or not.

        We define the usage of capitals in a word to be right when one of the following cases holds:

        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital, like "Google".
        Otherwise, we define that this word doesn't use capitals in a right way.

        Args:
            word (str): [description]

        Returns:
            bool: [description]
        """
        if len(word) == 1 or word.isupper() or word.islower():
            return True
        
        if word[0].isupper() and word[1:].islower():
            return True


def main():
    s = Solution()
    word =  'USA'
    ans = s.detectCapitalUse(word)
    print(ans)


if __name__ == '__main__':
    main()
