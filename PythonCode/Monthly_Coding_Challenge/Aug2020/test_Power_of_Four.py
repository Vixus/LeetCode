from Add_and_Search_Word___Trie import WordDictionary


def test1():
    solArr = []
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')
    solArr.append(obj.search('pad'))
    solArr.append(obj.search('bad'))
    solArr.append(obj.search('.ad'))
    solArr.append(obj.search('b..'))
    assert solArr == [False, True, True, True]
