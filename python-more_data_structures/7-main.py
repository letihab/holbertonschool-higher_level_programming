#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted(new_dict)
print("--")
print_sorted(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted(new_dict)
print("--")
print_sorted(a_dictionary)
