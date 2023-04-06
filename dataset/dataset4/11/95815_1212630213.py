import ctypes
import os
import tempfile

RtlGetLastNtStatus = ctypes.WinDLL('ntdll').RtlGetLastNtStatus
STATUS_FILE_IS_A_DIRECTORY = ctypes.c_long(0xC000_00BA).value

def test():
    path = tempfile.mkdtemp()
    try:
        os.remove(path)
    except PermissionError as e:
        if RtlGetLastNtStatus() != STATUS_FILE_IS_A_DIRECTORY:
            raise
        raise IsADirectoryError(errno.EISDIR,
                                os.strerror(errno.EISDIR),
                                e.filename,
                                e.winerror)