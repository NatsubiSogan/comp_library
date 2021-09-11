#include <string>
#include <vector>

std::vector<int> manacher(const std::string& s) {
	int i = 0, j = 0;
	std::vector<int> res((int)s.size(), 0);
	while (i < (int)s.size()) {
		while (i - j >= 0 && i + j < (int)s.size() && s[i - j] == s[i + j]) j++;
		res[i] = j;
		int k = 1;
		while (i - k >= 0 && i + k < (int)s.size() && k + res[i - k] < j) {
			res[i + k] = res[i - k];
			k++;
		}
		i += k;
		j -= k;
	}
	return res;
}