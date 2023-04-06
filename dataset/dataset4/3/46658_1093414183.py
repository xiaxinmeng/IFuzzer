import gzip
f_in = open('/home/joe/file.txt', 'rb')
f_out = gzip.open('/home/joe/file.txt.gz', 'wb');
f_out.writelines(f_in)
file_obj_out.close()
f_out.close()