# SlidingWindowAggretgation
class SlidingWindowAggretgation:
	def __init__(self, op) -> None:
		self.op = op
		self.front_stack = []
		self.back_stack = []

	def __len__(self) -> int:
		return len(self.front_stack) + len(self.back_stack)

	def __bool__(self) -> bool:
		return len(self) > 0

	def __str__(self) -> str:
		data = [x for x, _ in self.front_stack][::-1] + [x for x, _ in self.back_stack]
		return str(data)

	def append(self, x: int) -> None:
		fx = x
		if self.back_stack:
			fx = self.op(self.back_stack[-1][1], x)
		self.back_stack.append((x, fx))

	def popleft(self) -> None:
		if not self.front_stack:
			x = fx = self.back_stack.pop()[0]
			self.front_stack.append((x, fx))
			while self.back_stack:
				x = self.back_stack.pop()[0]
				fx = self.op(x, fx)
				self.front_stack.append((x, fx))
		self.front_stack.pop()

	def all_prod(self) -> int:
		res = None
		if self.front_stack:
			res = self.front_stack[-1][1]
		if self.back_stack:
			if res is None:
				res = self.back_stack[-1][1]
			else:
				res = self.op(res, self.back_stack[-1][1])
		return res
