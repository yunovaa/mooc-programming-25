# Write your solution here
import math 

def dict_of_numbers():
    digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    
    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 
            70: 'seventy', 80: 'eighty', 90: 'ninety'}
    d = {}

    for i in range(20):
        if i in digits:
            d[i] = digits[i]
        elif i in teens:
            d[i] = teens[i]
    
    for i in range(20, 100):
        if not i%10:
            d[i] = tens[i]
        else:
            d[i] = f"{tens[i-i%10]}-{digits[i%10]}"

    return d

