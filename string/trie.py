import collections

# Trie
class TrieNode:
	def __init__(self):
		self.child = collections.defaultdict(TrieNode)
		self.is_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word: str) -> None:
		cur = self.root
		for letter in word:
			cur = cur.child[letter]
		cur.is_word = True

	def search(self, word: str) -> bool:
		cur = self.root
		for letter in word:
			cur = cur.child.get(letter)
			if cur == None:
				return False
		return cur.is_word

	def starts_with(self, prefix: str) -> bool:
		cur = self.root
		for letter in prefix:
			cur = cur.child.get(letter)
			if cur == None:
				return False
		return True