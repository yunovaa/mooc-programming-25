# Write your solution here
import re

def is_dotw(my_string: str):
    return True if re.search('(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', my_string) else False

def all_vowels(my_string: str):
    return True if re.match('^[aeuio]+$', my_string) else False

def time_of_day(my_string: str):
    return True if re.match('([0-1][0-9]|2[0-4]):([0-5][0-9]):([0-5][0-9])', my_string) else False