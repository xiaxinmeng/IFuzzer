def pipe_cloexec(self):
            """Create a pipe with FDs set CLOEXEC."""
            # Pipes' FDs are set CLOEXEC by default because we don't want them
            # to be inherited by other subprocesses: the CLOEXEC flag is removed
            # from the child's FDs by _dup2(), between fork() and exec().
            # This is not atomic: we would need the pipe2() syscall for that.
            r, w = os.pipe()
            self._set_cloexec_flag(r)
            self._set_cloexec_flag(w)
            return r, w