# now save list to a file:
# https://bbs.archlinux.org/viewtopic.php?id=75839
f = open("fileList.TXT", "w")
f.write("\n".join(map(lambda x: str(x), outList))) 
f.close()