atRegex = re.compile(r'...at*')
TextStr=(atRegex.findall(':at-at~at:  The Bigcat sat in the hat sat on the flat sat mat sat.'))
print('\nFull Text String:---> :at-at~at: The Bigcat sat in the hat sat on the flat sat mat sat mat\n')
print('\n Greedy Mode: Returns\n' +  ':---> ' + str(TextStr)+'\n')