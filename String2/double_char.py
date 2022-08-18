'''
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

'''
def double_char(str):
    str2 = ''
    for dc in str:
        str2 = str2 + dc + dc
    return str2
    #new_str = "".join([i+j for i,j in zip(list(str),list(str))])
print(double_char('sunil'))