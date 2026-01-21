
def balanced_brackets(my_string: str):

    my_string = help_strip(my_string)
    print(my_string)

    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not(my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


def help_strip(my_string: str):
    return ''.join([s for s in my_string if s in '()[]'])

