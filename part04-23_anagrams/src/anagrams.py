# Write your solution here

def anagrams(s_1, s_2):
    s_1 = sorted(s_1)
    s_2 = sorted(s_2)
    if len(s_1) == len(s_2):
        for i in range(len(s_2)):
            if s_2 == s_1:
                continue
            return False
        return True
    return False
        