if zinfo.isdir():
    # 0755 + MS-DOS directory flag
    zinfo.external_attr = 0o755 | 0x010
else:
    zinfo.external_attr = 0o644