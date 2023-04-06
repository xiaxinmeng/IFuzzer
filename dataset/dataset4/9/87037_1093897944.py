import re
text="aba"
#match=re.search(r"(b\2|(a))*",text) - not worked
match=re.search(r"((a)|b\2)*",text)
if(match):
    #show aba ba a
    print(match.group(0)+" "+match.group(1)+" "+match.group(2))