def unique(seq):
	"""Dict of unique values (keys) & their counts in original sequence"""

	out_dict = dict.fromkeys(set(seq), 0)
	for i in seq:
		out_dict[i] += 1
	return out_dict


iterable = list(range(43)) + list(range(43, 0, -1))