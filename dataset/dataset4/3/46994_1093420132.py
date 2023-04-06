def iswow64():
    if platform.getarchitecture()[0] == '64-bit':return False
    return os.environ["PROCESSOR_ARCHITECTURE"] != "x86"