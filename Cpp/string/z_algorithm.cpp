#include <string>
#include <vector>

std::vector<int> z_algorithm(const std::string& s) {
	int len = (int)s.size();
	std::vector<int> res(s.size());
	res[0] = s.size();
	int i = 1, j = 0;
	while (i < s.size()) {
		while (i + j < s.size() && s[i + j] == s[j]) j++;
		res[i] = j;
		if (j == 0) {
			i++;
			continue;
		}
		int k = 1;
		while (i + k < s.size() && j > k + res[k]) {
			res[i + k] = res[k];
			k++;
		}
		i += k;
		j -= k;
	}
	return res;
}