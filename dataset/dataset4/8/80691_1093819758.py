import re
    #_____________
    #Normal Mode
    #_____________

atRegex = re.compile(r'...at')
TextStr=(atRegex.findall(':at-at~at:  The Bigcat sat in the hat sat on the flat sat mat sat.'))
print('\nFull Text String:---> :at-at~at: The Bigcat sat in the hat sat on the flat sat mat sat\n')
print('\n Normal Mode: Returns\n' +  ':--->' + str(TextStr))