import resource
MAX_VIRTUAL_MEMORY = 1 * 1024 * 1024
resource.setrlimit(resource.RLIMIT_VMEM, (MAX_VIRTUAL_MEMORY, MAX_VIRTUAL_MEMORY))