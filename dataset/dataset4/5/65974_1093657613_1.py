if os.path.exists('/mnt/example_nt'):
    print('cleaning up')
    shutil.rmtree('/mnt/example_nt')

print('copying')
shutil.copytree('PC/example_nt', '/mnt/example_nt')
EOF