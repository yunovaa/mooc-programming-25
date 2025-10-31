# Write your solution here

def most_common_character(s):

    l = list(s)
    mx_ls = []
    for i in l:
        mx_ls.append(l.count(i))
    
    return l[mx_ls.index(max(mx_ls))]

