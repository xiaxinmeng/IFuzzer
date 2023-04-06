source_path = Path('../data')
destination_path = Path('//file_server/work/whatever')
for file_name in source_path.glob('xyz-*'):
    shutil.copyfile(source_path / file_name, destination_path / file_name)