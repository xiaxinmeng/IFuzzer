free = st.f_bavail * st.f_bsize
total = st.f_blocks * st.f_frsize
used = (total - st.f_bfree * st.f_bsize)