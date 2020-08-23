"""
Implement the StreamChecker class as follows:
StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

Example:
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 
Note:
1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""


from typing import List
from collections import deque


class Trie:
    def __init__(self):
        self.children = {}
        self.endNode = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.queryArr = ''

        for word in words:
            node = self.root
            for letter in reversed(word):
                node = node.children.setdefault(letter, Trie())
            node.endNode = True

    def query(self, letter: str) -> bool:
        self.queryArr = self.queryArr + letter
        node = self.root

        for char in reversed(self.queryArr):
            if char in node.children:
                node = node.children[char]
                if node.endNode == True:
                    return True
            else:
                break

        return False

    # THIS SOLUTION IS TOO SLOW
    # def __init__(self, words: List[str]):
    #     self.root = Trie()
    #     self.de = deque()

    #     for word in words:
    #         node = self.root
    #         for letter in word:
    #             node = node.children.setdefault(letter, Trie())
    #         node.endNode = True

    # def query(self, letter: str) -> bool:
    #     foundWord = False
    #     self.de.appendleft(self.root)

    #     for _ in range(len(self.de)):
    #         node = self.de.pop()
    #         if letter in node.children:
    #             self.de.appendleft(node.children[letter])
    #             if node.children[letter].endNode == True:
    #                 foundWord = True

    #     return foundWord

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


def main():
    streamChecker = StreamChecker(["cd", "f", "kl"])
    print(streamChecker.query('a'))
    print(streamChecker.query('b'))
    print(streamChecker.query('c'))
    print(streamChecker.query('d'))  # True
    print(streamChecker.query('e'))
    print(streamChecker.query('f'))  # True
    print(streamChecker.query('g'))
    print(streamChecker.query('h'))
    print(streamChecker.query('j'))
    print(streamChecker.query('k'))
    print(streamChecker.query('l'))  # True


if __name__ == '__main__':
    main()
