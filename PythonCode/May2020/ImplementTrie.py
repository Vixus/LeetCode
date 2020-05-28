class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.

    Trie trie = new Trie();

    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");   
    trie.search("app");     // returns true
    """

    def convertToNum(self, letter):
        return ord(letter)-ord('a')

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None]*26
        self.endOfWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self
        for x in word:
            index = ptr.convertToNum(x)
            if not ptr.children[index]:
                ptr.children[index] = Trie()

            ptr = ptr.children[index]

        ptr.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self
        found = False
        for i, x in enumerate(word):
            index = ptr.convertToNum(x)
            if ptr.children[index]:
                ptr = ptr.children[index]
                if i == len(word)-1:
                    if ptr.endOfWord:
                        found = True
            else:
                break

        return found

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self
        found = False
        for i, x in enumerate(prefix):
            index = ptr.convertToNum(x)
            if ptr.children[index]:
                ptr = ptr.children[index]
                if i == len(prefix)-1:
                    found = True
            else:
                break

        return found


def main():
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert('apple')
    print(obj.search('app'))
    print(obj.startsWith('app'))


if __name__ == '__main__':
    main()
