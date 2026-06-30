class PrefixTree:
    def __init__(self):
        self.set = set()

    def insert(self, word: str) -> None:
        self.set.add(word)

    def search(self, word: str) -> bool:
        if word in self.set:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return any(word.startswith(prefix) for word in self.set)
        