if get_platform() in ["solaris-2.9-sun4u", "linux-x86_64"]:
    os.environ["CFLAGS"] = "-fPIC"