path = "c:\\" + "\\".join (130 * ['xx'])
os.makedirs (path)
#
# will fail more or less violently
#
path = "\\\\?\\" + path
os.makedirs (path)
os.listdir (path)