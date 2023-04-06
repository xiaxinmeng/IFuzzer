
import zipfile
file_path = "/tmp/test_folder/test.md"
rel_name = "test.md"
zfile = zipfile.ZipFile("tmp.zip",'w')
zif = zipfile.ZipInfo("tmp/")
zfile.writestr(zif,"")
zfile.write(file_path, rel_name)
zfile.close()
