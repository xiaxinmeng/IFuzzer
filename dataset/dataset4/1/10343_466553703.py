
def custom_formatwarning(msg, *a):
    # ignore everything except the message
    return '\nWarning: ' + str(msg) + '\n'

warnings.formatwarning = custom_formatwarning
