def merge(intervals):
    
    intervals.sort(key = lambda x:x[0])
    print(intervals)
    merged = []
    for interval in intervals:
        
        if not merged or merged[-1][1] <interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1] , interval[1])
    return merged 
 
intervals = [[1,6],[3,5],[2,3],[8,10]]
print("Merged Intervals : " , merge(intervals))        