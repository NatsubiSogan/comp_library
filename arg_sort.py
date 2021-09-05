import functools

# 偏角ソート
def sort_by_argument(points: list) -> list:
	def compare(p1: tuple, p2: tuple) -> int:
		x1, y1 = p1; x2, y2 = p2
		tmp = x1 * y2 - y1 * x2
		if tmp < 0: return 1
		elif tmp > 0: return -1
		else: return 0

	quad = [[] for i in range(4)]

	for x, y in points:
		if x == y == 0: quad[2].append((x, y))
		elif x <= 0 and y < 0: quad[0].append((x, y))
		elif x > 0 and y <= 0: quad[1].append((x, y))
		elif x >= 0 and y > 0: quad[2].append((x, y))
		else: quad[3].append((x, y))
	
	res = []

	for i in range(4):
		quad[i].sort(key=functools.cmp_to_key(compare))
		for point in quad[i]: res.append(point)
	
	return res