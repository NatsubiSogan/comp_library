import collections

# Trie
class TrieNode:
	def __init__(self):
		self.child = collections.defaultdict(TrieNode)
		self.is_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		cur = self.root
		for letter in word:
			cur = cur.child[letter]
		cur.is_word = True

	def search(self, word):
		cur = self.root
		for letter in word:
			cur = cur.child.get(letter)
			if cur == None:
				return False
		return cur.is_word

	def startsWith(self, prefix):
		cur = self.root
		for letter in prefix:
			cur = cur.child.get(letter)
			if cur == None:
				return False
		return True