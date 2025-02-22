# Homework for the Topic "Prefix Trees"

## Task 1. Extending Trie Functionality

Implement two additional methods for the `Trie` class:

- `count_words_with_suffix(pattern)` to count the number of words that end with the given pattern;
- `has_prefix(prefix)` to check if there are words with the given prefix.

### Technical Requirements

- The `Homework` class must inherit from the base `Trie` class.
- The methods must handle errors related to incorrect input data.
- The input parameters for both methods must be strings.
- The `count_words_with_suffix` method must return an integer.
- The `has_prefix` method must return a boolean value.

### How to Run
```
python task_1.py
```

## Task 2. Finding the Longest Common Prefix

Create a `LongestCommonWord` class that inherits from `Trie` and implement the `find_longest_common_word` method, which finds the longest common prefix among all words in the input list of strings `strings`.

### Technical Requirements

- The `LongestCommonWord` class must inherit from `Trie`.
- The input parameter of the `find_longest_common_word` method, `strings`, is a list of strings.
- The `find_longest_common_word` method must return a string representing the longest common prefix.
- The time complexity must be O(S), where S is the total length of all strings.

### How to Run
```
python task_2.py
```
