for name in names:
    try:
        # Here, we don't use AT_SYMLINK_NOFOLLOW to be consistent with
        # walk() which reports symlinks to directories as directories.
        # We do however check for symlinks before recursing into
        # a subdirectory.
        if st.S_ISDIR(stat(name, dir_fd=topfd).st_mode):
            dirs.append(name)
        else:
            nondirs.append(name)
    except FileNotFoundError:
        try:
            # Add dangling symlinks, ignore disappeared files
            if st.S_ISLNK(stat(name, dir_fd=topfd, follow_symlinks=False)
                        .st_mode):
                nondirs.append(name)
        except FileNotFoundError:
            continue