#BEGIN: WTF
a_str_whole = fs_in.read()
fs_in.close()
a_str_lines = a_str_whole.split("\n")
for idx in range(0,len(a_str_lines)-1):
   a_str_lines[idx]+="\n"
#END: WTF