import typing

# 永続配列
class PersistentArrayNode:
	def __init__(self, log: int) -> None:
		self.val = None
		self.ch = [None] * (1 << log)

class PersistentArray:
	def __init__(self, log: int = 4) -> None:
		self.log = log
		self.mask = (1 << log) - 1

	def build(self, array: list) -> typing.Union[PersistentArrayNode, None]:
		rt = None
		for i, val in enumerate(array):
			rt = self.init_set(i, val, rt)
		return rt

	def init_set(self, i: int, val: typing.Any, t: typing.Union[PersistentArrayNode, None]) -> PersistentArrayNode:
		if t is None:
			t = PersistentArrayNode(self.log)
		if i == 0:
			t.val = val
		else:
			t.ch[i & self.mask] = self.init_set(i >> self.log, val, t.ch[i & self.mask])
		return t

	def set(self, i: int, val: typing.Any, t: int) -> PersistentArrayNode:
		res = PersistentArrayNode(self.log)
		if t is not None:
			res.ch = t.ch[:]
			res.val = t.val
		if i == 0:
			res.val = val
		else:
			res.ch[i & self.mask] = self.set(i >> self.log, val, res.ch[i & self.mask])
		return res
		
	def get(self, i: int, t: int) -> typing.Any:
		if i == 0:
			return t.val
		else:
			return self.get(i >> self.log, t.ch[i & self.mask])
