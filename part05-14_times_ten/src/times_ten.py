# Write your solution here
def times_ten(start_index: int, end_index: int):
    return {key: key*10 for key in range(start_index, end_index+1)}