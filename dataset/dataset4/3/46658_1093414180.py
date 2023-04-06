# Example of how to decompress a file
import gzip
file_obj = gzip.GzipFile('/home/joe/file.txt.gz', 'rb');
file_content = file_obj.read()
file_obj.close()

# Example of how to create a compressed GZIP file
import gzip
file_content = "Lots of content here"
file_obj = gzip.GzipFile('/home/joe/file.txt.gz', 'wb');
file_obj.write(file_content)
file_content.close()

# Example of how to compress an existing file
import shutil
import gzip
file_obj_in = file('/home/joe/file.txt', 'rb')
file_obj_out = gzip.GzipFile('/home/joe/file.txt.gz', 'wb');
shutil.copyfileobj(file_obj_in, file_obj_out)
file_obj_out.close()