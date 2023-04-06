fp = open("bug_out.txt", "ab")
buff = 'Hello world'
print('type of buff is', type(buff))
bin_buff = bytes(buff,  'utf-8')
print('type of bin_buff is', type(bin_buff))
print(bin_buff, file=fp)