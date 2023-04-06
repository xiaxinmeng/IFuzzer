class signalfd_siginfo(Structure):
    _fields_ = (
        ('ssi_signo', c_uint32),    # Signal number
        ('ssi_errno', c_int32),     # Error number (unused)
        ('ssi_code', c_int32),      # Signal code
        ('ssi_pid', c_uint32),      # PID of sender
        ('ssi_uid', c_uint32),      # Real UID of sender
        ('ssi_fd', c_int32),        # File descriptor (SIGIO)
        ('ssi_tid', c_uint32),      # Kernel timer ID (POSIX timers)
        ('ssi_band', c_uint32),     # Band event (SIGIO)
        ('ssi_overrun', c_uint32),  # POSIX timer overrun count
        ('ssi_trapno', c_uint32),   # Trap number that caused signal
        ('ssi_status', c_int32),    # Exit status or signal (SIGCHLD)
        ('ssi_int', c_int32),       # Integer sent by sigqueue(2)
        ('ssi_ptr', c_uint64),      # Pointer sent by sigqueue(2)
        ('ssi_utime', c_uint64),    # User CPU time consumed (SIGCHLD)
        ('ssi_stime', c_uint64),    # System CPU time consumed (SIGCHLD)
        ('ssi_addr', c_uint64),     # Address that generated signal
                                    # (for hardware-generated signals)
        ('_padding', c_char * 46),  # Pad size to 128 bytes (allow for
                                    # additional fields in the future)
    )