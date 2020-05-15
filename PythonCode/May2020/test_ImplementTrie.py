from ImplementTrie import Trie


def test1():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True


def test2():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("app") == False


def test3():
    trie = Trie()
    trie.insert("apple")
    assert trie.startsWith("app") == True


def test4():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    assert trie.search("app") == True
