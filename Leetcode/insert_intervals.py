def insert_interval(intervals, new):
    res = []
    i = 0
    n = len(intervals)
    # add all intervals before new
    while i < n and intervals[i][1] < new[0]:
        res.append(intervals[i])
        i += 1
    # merge overlapping intervals
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    res.append(new)
    # add the rest
    while i < n:
        res.append(intervals[i])
        i += 1
    return res

