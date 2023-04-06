import os
import shutil
import tarfile
import tempfile

def test_tar_overwrites_symlink():
    d = tempfile.mkdtemp()
    try:
        new_dir_name = os.path.join(d, 'newdir')
        archive_name = os.path.join(d, 'newdir.tar')
        os.mkdir(new_dir_name)
        source_file_name = os.path.join(new_dir_name, 'source')
        target_link_name = os.path.join(new_dir_name, 'symlink')
        with open(source_file_name, 'w') as f:
            f.write('something\n')
        os.symlink(source_file_name, target_link_name)
        with tarfile.open(archive_name, 'w') as tar:
            for f in [source_file_name, target_link_name]:
                tar.add(f, arcname=os.path.basename(f))
        # this should not raise OSError: [Errno 17] File exists
        with tarfile.open(archive_name, 'r') as tar:
            tar.extractall(path=new_dir_name)
    finally:
        shutil.rmtree(d)