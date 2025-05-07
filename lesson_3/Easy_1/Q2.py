# How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def ends_with_exclamation(string):
    if string[-1] == '!':
        print('True')
    elif string[-1] != '!':
        print('False')
    
ends_with_exclamation(str1)