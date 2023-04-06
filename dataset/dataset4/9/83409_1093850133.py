
import traceback


class CrashingRepr:
    def __repr__(self):
        raise RuntimeError("crash")


traceback.FrameSummary("fname", 1, "name", locals={"crash": CrashingRepr()})
