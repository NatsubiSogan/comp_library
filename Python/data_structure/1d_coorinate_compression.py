# 1次元座標圧縮
def one_d_coordinate_compression(l: list) -> list:
	n = len(l)
	sorted_list = sorted(set(l))
	d = {sorted_list[i]: i for i in range(len(sorted_list))}
	return [d[i] for i in l]