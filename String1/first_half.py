'''
Given a string of even length, 
return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

'''
def first_half(str):
    h = int(len(str)/2)
    return print(str[0:h])

first_half('hello!')
