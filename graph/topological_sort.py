# トポロジカルソート
def topological_sort(G: list, d: list) -> list:
	n = len(G)
	s = []
	for i in range(n):
		if d[i] == 0: s.append(i)
	ans = []
	while s:
		u = s.pop()
		ans.append(u)
		for v in G[u]:
			d[v] -= 1
			if d[v] == 0: s.append(v)
	if len(ans) != n: return -1
	return ans