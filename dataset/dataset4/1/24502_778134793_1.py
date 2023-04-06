
if build_os.startswith("linux-musl"):
    PLATFORM_TRIPLET = PLATFORM_TRIPLET.replace("linux-gnu", "linux-musl")
