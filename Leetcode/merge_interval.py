intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):
	if not intervals:
		return []
	intervals_sorted = sorted(intervals, key=lambda x: x[0])
	merged = [intervals_sorted[0][:]]
	for current in intervals_sorted[1:]:
		last = merged[-1]
		if current[0] <= last[1]:
			last[1] = max(last[1], current[1])
		else:
			merged.append(current[:])
	return merged

merged = merge_intervals(intervals)

print(merged)  # Output: [[1, 6], [8, 10], [15, 18]]