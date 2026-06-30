class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, c) -> str:
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = self._char_to_index(c)
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = self._char_to_index(c)
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = self._char_to_index(c)
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True
        