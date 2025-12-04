# Write your solution here
import string

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def equal(a, b):
    return True if a==b else False

def not_equal(a, b):
    return True if a!=b else False

def gt(a, b):
    return True if a>b else False

def st(a, b):
    return True if a<b else False

def gte(a, b):
    return True if a>=b else False

def ste(a, b):
    return True if a<=b else False

def run(program):

    l = []
    variables = {letter: 0 for letter in string.ascii_uppercase}
    op = {'ADD': sum, 'SUB': sub, 'MUL': mul}
    locations = {label[:-1]: index for index, label in enumerate(program) if len(label.split())==1 and label != 'END'}
    comparisons = {'==': equal, '!=':not_equal,'>':gt,'<':st,'>=':gte,'<=':ste}
    pointer = 0

    def check_int_or_variable(value):
        if value in variables.keys():
            value = variables[value]
        else:
            value = int(value)
        return value
    
    def has_more_lines():
        return True if len(program)>pointer else False        

    while has_more_lines():

        line = program[pointer]
        #print(f'executing line: {pointer}, {line}')

        if line.startswith('PRINT'):
            l.append(check_int_or_variable(line.split()[-1]))
            #print(f'updated list: {l}')

        elif line.startswith('MOV'):
            variable, value = line.split()[1:]
            variables[variable] = check_int_or_variable(value)

        elif line.split()[0] in op.keys():
            operation, variable, value = line.split()
            variables[variable] = op[operation](variables[variable], check_int_or_variable(value))

        elif line.startswith('JUMP'):
            label = line.split()[-1]
            pointer = locations[label]
            continue

        elif line.startswith('IF'):
            label = line.split()[-1]
            cond = line.split('JUMP')[0].split('IF')[-1]
            value_1, comparison, value_2 = cond.split()
            value_1 = check_int_or_variable(value_1)
            value_2 = check_int_or_variable(value_2)
            if comparisons[comparison](value_1, value_2):
                pointer = locations[label]
                continue

        elif line == 'END':
            return l
        
        pointer+=1

    return l
        


if __name__ == '__main__':
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)