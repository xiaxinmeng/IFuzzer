class MyDerivedClass(MyPurePythonClass,MyBoostClass):
        def __init__(self):
                MyPurePythonClass.__init__(self)
                MyBoostClass.__init__(self)