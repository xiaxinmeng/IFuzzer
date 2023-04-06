
import resource
resource.setrlimit(resource.RLIMIT_STACK, resource.getrlimit(resource.RLIMIT_STACK))
