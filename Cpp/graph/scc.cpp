#include <algorithm>
#include <vector>

struct strongly_connected_components {
	public:
		strongly_connected_components() = default;
		explicit strongly_connected_components(int n) : G(n), G_rev(n), comp(n, -1), visited(n), rev_visited(n) {}

		void add_edge(int u, int v) {
			G[u].push_back(v);
			G_rev[v].push_back(u);
		}

		void build() {
			for (int i = 0; i < (int)G.size(); i++) {
				if (!visited[i]) dfs(i);
			}
			std::reverse(order.begin(), order.end());
			cnt = 0;
			for (int i : order) {
				if (!rev_visited[i]) rev_dfs(i, cnt++);
			}
		}

		int operator[](const int& i) {
			return comp[i];
		}

		int count() {
			return cnt;
		}

	private:
		std::vector<std::vector<int>> G, G_rev;
		std::vector<int> comp, order;
		std::vector<bool> visited, rev_visited;
		int cnt;

		void dfs(int u) {
			visited[u] = true;
			for (int v : G[u]) {
				if (!visited[v]) dfs(v);
			}
			order.push_back(u);
		}

		void rev_dfs(int u, int c) {
			rev_visited[u] = true;
			comp[u] = c;
			for (int v : G_rev[u]) {
			  if (!rev_visited[v]) rev_dfs(v, c);
			} 
		}
};