from Iterator_for_Combination import CombinationIterator


def test1():
    input = 'abc'
    iterator = CombinationIterator(input, 2)
    assert iterator.next() == 'ab'
    assert iterator.hasNext() == True
    assert iterator.next() == 'ac'
    assert iterator.hasNext() == True
    assert iterator.next() == 'bc'
    assert iterator.hasNext() == False
