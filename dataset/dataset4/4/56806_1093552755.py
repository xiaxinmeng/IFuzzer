def ill(row):
  row[1]=1
list_manual=[[0,0,0],[0,0,0],[0,0,0]]
list_generated=[[0,0,0]]*3
ill(list_manual[1])
print(list_manual)
ill(list_generated[1])
print(list_generated)