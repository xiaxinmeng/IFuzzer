def strcoll_case_sensitive(string1,string2):
    """ This function was written because string comparisons
in Windows 
        seem to be case insensitive if the string is longer
than 
        one character. """
    # First, compare the first character
    diff = locale.strcoll(string1[0],string2[0])
    if diff == 0:
        # If the first character is the same, compare the rest
        diff = locale.strcoll(string1,string2)
    return diff