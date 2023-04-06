modes = []
for m in [msvcrt.CRT_WARN, msvcrt.CRT_ERROR, msvcrt.CRT_ASSERT]:
    oldmode = msvcrt.CrtSetReportMode(m, 0)
    msvcrt.CrtSetReportMode(m, oldmode)
    modes.append((m, oldmode))