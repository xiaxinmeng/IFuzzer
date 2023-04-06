def my_input():
    return input("Enter data or return to stop: ")
for data in iter(my_input, ''):
    process(data)