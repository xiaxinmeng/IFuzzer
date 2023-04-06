for name in names:
    # Here, we don't use AT_SYMLINK_NOFOLLOW to be consistent with
    # walk() which reports symlinks to directories as directories. We do
    # however check for symlinks before recursing into a subdirectory.
    if st.S_ISDIR(fstatat(topfd, name).st_mode):
        dirs.append(name)
    else:
        nondirs.append(name)