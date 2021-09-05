# SCC
def strongly_connected_component(G: list) -> list:
	n = len(G)
	G_rev = [[] for i in range(n)]
	for i in range(n):
		for v in G[i]:
			G_rev[v].append(i)
	vs = []
	visited = [False] * n
	def dfs(v):
		visited[v] = True
		for u in G[v]:
			if not visited[u]:
				dfs(u)
		vs.append(v)
	for i in range(n):
		if not visited[i]:
			dfs(i)
	rev_visited = [False] * n
	def rev_dfs(v):
		p.append(v)
		rev_visited[v] = True
		for u in G_rev[v]:
			if not rev_visited[u]:
				rev_dfs(u)
	res = []
	for v in vs[::-1]:
		if not rev_visited[v]:
			p = []
			rev_dfs(v)
			res.append(p)
	return res
