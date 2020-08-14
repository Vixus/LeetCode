"""
Design an Iterator class, which has:
A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.

Example:
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:
1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

Hide Hint #1
Generate all combinations as a preprocessing.

Hide Hint #2
Use bit masking to generate all the combinations.
"""

from typing import List
from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = [''.join(c) for c in combinations(
            characters, combinationLength)]

    def next(self) -> str:
        return self.combs.pop(0)

    def hasNext(self) -> bool:
        return bool(self.combs)

        # Your CombinationIterator object will be instantiated and called as such:
        # obj = CombinationIterator(characters, combinationLength)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()


def main():
    iterator = CombinationIterator("abc", 2)
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())


if __name__ == '__main__':
    main()
