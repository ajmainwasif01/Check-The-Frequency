test_dictionary = {
    'Codingal': 3,  'is': 2,'best': 2, 'for': 2,'Coding': 1
}

print("Test Dictionary:", test_dictionary)

value_to_check = int(input("Enter the value to check its frequency: "))

frequency = list(test_dictionary.values()).count(value_to_check)

print(f"The frequency of the value {value_to_check} is: {frequency}")
