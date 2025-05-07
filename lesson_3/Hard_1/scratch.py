# 2.  Advanced: Write a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the number of times each string appears in the list. Then, create a second function that returns a dictionary of only the strings that appear more than once, with their frequencies.

test_list = ['tom', 'jerry', 'tom', 'once again', 'jerr two']

def list_to_dict(list):
    new_dict = {}
    for item in list:
        new_dict[item] = list.count(item)
    return new_dict

def only_multiples_in_dict(dict):
    multiples_dict = {}
    for key, value in dict.items():
        if value > 1:
            multiples_dict[key] = value
    return multiples_dict


print(only_multiples_in_dict(list_to_dict(test_list)))