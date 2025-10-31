# Write your solution here
def count_matching_elements(m, a):
    c = 0
    for i in m:
        for j in i:
            if j == a:
                c+=1
    return c