class MyBreakpoint (gdb.Breakpoint):
    def stop(self):
        # frame of the caller
        frame = gdb.selected_frame()
        frame = frame.older()

        name = frame.name()
        if name == '_PyCFunction_FastCallKeywords':
            pass
        else:
            # callable->ob_type
            obj = frame.read_var('callable')
            obj = obj.referenced_value()['ob_type']

            obj2 = gdb.lookup_global_symbol('PyType_Type').value()

            if obj == obj2.address:
                return False

            print("don't skip", obj, obj2.address)

        gdb.execute("up")
        return True


MyBreakpoint("_PyStack_AsTuple")
MyBreakpoint("_PyStack_AsDict")