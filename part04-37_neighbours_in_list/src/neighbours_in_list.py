# Write your solution here
def longest_series_of_neighbours(l):
    c, mx = 1, 0
    for i in range(0, len(l)-1):
        if abs(l[i] - l[i+1]) == 1:
            c+=1
        else:
            c = 1
        mx = max(c, mx)
    return mx

