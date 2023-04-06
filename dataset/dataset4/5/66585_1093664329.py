filename = "sample.msp"
patch_database = msilib.OpenDatabase(filename, msilib.MSIDBOPEN_READONLY | msilib.MSIDBOPEN_PATCHFILE)
summary_info = patch_database.GetSummaryInformation(20)
print (summary_info.GetProperty(msilib.PID_REVNUMBER))