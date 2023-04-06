class OurLogStdErr:
    def write (self, txt):
        printLog (txt, PRINT_ERROR)
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
class OurLogStdOut:
    def write (self, txt):
        printLog (txt)