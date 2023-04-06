def _patchheader(self):
        self._file.seek(8)
        # jjk added * sampwidth otherwise for 16 bit you get wrong nframes
        _write_u32(self._file, self._datawritten*self._sampwidth)
        self._datalength = self._datawritten
        self._file.seek(0, 2)