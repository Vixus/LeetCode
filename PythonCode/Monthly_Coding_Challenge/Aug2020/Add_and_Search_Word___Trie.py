class Trie:
    def __init__(self):
        self.children = {}
        self.endNode = False


class WordDictionary:
    """
    Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

    Example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
    Note:
    You may assume that all words are consist of lowercase letters a-z.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for letter in word:
            root = root.children.setdefault(letter, Trie())
        root.endNode = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, i):
            if i == len(word):
                return node.endNode

            if word[i] == '.':
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)

            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


def main():
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')
    print(obj.search('pad'))
    print(obj.search('bad'))
    print(obj.search('.ad'))
    print(obj.search('b..'))


if __name__ == '__main__':
    main()
