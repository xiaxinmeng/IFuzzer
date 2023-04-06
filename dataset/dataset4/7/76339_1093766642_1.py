@suppress(FileNotFoundError)
def is_docker():
	return (
		os.path.exists('/.dockerenv')
		or any('docker' in line for line in open('/proc/self/cgroup'))
	)