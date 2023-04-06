def withpythonimplementation(testfunc):
    def newtest(self):
        # Test default implementation
        testfunc(self)
        # Test Python implementation
        if quopri.b2a_qp is not None or quopri.a2b_qp is not None:
            oldencode = quopri.b2a_qp
            olddecode = quopri.a2b_qp
            try:
                quopri.b2a_qp = None
                quopri.a2b_qp = None
                testfunc(self)
            finally:
                quopri.b2a_qp = oldencode
                quopri.a2b_qp = olddecode
    newtest.__name__ = testfunc.__name__
    return newtest