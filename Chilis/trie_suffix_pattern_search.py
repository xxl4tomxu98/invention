""" Pattern Searching using a Trie of all Suffixes

Problem Statement: Given a text txt[0..n-1] and a pattern pat[0..m-1],
write a function search(char pat[], char txt[]) that prints all occurrences
of pat[] in txt[]. You may assume that n > m.
As discussed in the previous post, we discussed that there are two ways
efficiently solve the above problem.
1) Preprocess Pattern: KMP Algorithm, Rabin Karp Algorithm, Finite Automata,
Boyer Moore Algorithm.
2) Preprocess Text: Suffix Tree

The best possible time complexity achieved by first (preprocssing pattern)
is O(n) and by second (preprocessing text) is O(m) where m and n are lengths
of pattern and text respectively.

Note that the second way does the searching only in O(m) time and it is
preferred when text doesn’t change very frequently and there are many search
queries. We have discussed Suffix Tree (A compressed Trie of all suffixes of
the Text).

Implementation of Suffix Tree may be time consuming for problems to be coded
in a technical interview or programming contexts. In this post simple
implementation of a Standard Trie of all Suffixes is discussed. The
implementation is close to suffix tree, the only thing is, it’s a simple
Trie instead of compressed Trie.

As discussed in Suffix Tree post, the idea is, every pattern that is present
in text (or we can say every substring of text) must be a prefix of one of all
possible suffixes. So if we build a Trie of all suffixes, we can find the
pattern in O(m) time where m is pattern length.

Building a Trie of Suffixes
1) Generate all suffixes of given text.
2) Consider all suffixes as individual words and build a trie.

Let us consider an example text “banana\0” where ‘\0’ is string termination
character. Following are all suffixes of “banana\0” banana\0
anana\0
nana\0
ana\0
na\0
a\0
\0
If we consider all of the above suffixes as individual words and build a Trie,
we get following.

How to search a pattern in the built Trie?
Following are steps to search a pattern in the built Trie.
1) Starting from the first character of the pattern and root of the Trie, do
following for every character.
…..a) For the current character of pattern, if there is an edge from the
current node, follow the edge.
…..b) If there is no edge, print “pattern doesn’t exist in text” and return.

2) If all characters of pattern have been processed, i.e., there is a path
from root for characters of the given pattern, then print all indexes
where pattern is present. To store indexes, we use a list with every node that
stores indexes of suffixes starting at the node."""


# node of trie consists char of word
class Node:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord


class Solution:
    def __init__(self):
        self.trie = None

    # build the trie
    def build(self, words):
        # top of the trie
        self.trie = Node({}, False)
        for word in words:
            current = self.trie
            for char in word:
                # if current node has no child, build it
                if not (char in current.children):
                    current.children[char] = Node({}, False)
                # has child, then move to the child node
                current = current.children[char]
            current.isWord = True

    def autocomplete(self, word):
        current = self.trie
        for char in word:
            if not (char in current.children):
                return []
            current = current.children[char]
        return self._findWordsFromNode(current, word)

    # this is depth first search in the tree
    def _findWordsFromNode(self, node, prefix):
        words = []
        # if the node is word then add it in the result
        if node.isWord:
            words += [prefix]
        # otherwise move to its children and recursively search
        for char in node.children:
            words += self._findWordsFromNode(node.children[char],
                                             prefix + char)
        return words


s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete(('do')))
