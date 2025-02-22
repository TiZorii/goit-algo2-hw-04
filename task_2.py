from Trie import Trie
from typing import List


class LongestCommonWord(Trie):
    def find_longest_common_word(self, list_strings: List[str]) -> str:
        if not all(isinstance(s, str) for s in list_strings):
            raise TypeError(
                f"Illegal argument {list_strings}: must be a list of strings"
            )

        self.put_list(list_strings)

        current, result = self.root, ""
        while len(current.children) == 1:
            result += list(current.children.keys())[0]
            current = list(current.children.values())[0]

        return result

    def put_list(self, list_of_strings):
        for index, word in enumerate(list_of_strings):
            self.put(word, index)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
