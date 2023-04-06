# define a function to capitalize s
def my_capitalize(s):
    """This function capitalizes the argument s and returns it"""
    the_first_letter = s[0]  # 0 means the first char
    the_rest_of_s = s[1:]  # 1: means from the second till the end
    the_first_letter_uppercased = the_first_letter.upper()  # upper makes the string uppercase
    the_rest_of_s_lowercased = the_rest_of_s.lower()  # lower makes the string lowercase
    s_capitalized = the_first_letter_uppercased + the_rest_of_s_lowercased  # + concatenates
    return s_capitalized