import _xxsubinterpreters as interpreters
import pickle


class C:
    pass


c = C()

interp_id = interpreters.create()
c_bytes = pickle.dumps(c)
interpreters.run_string(
    interp_id,
    "import pickle; pickle.loads(c_bytes)",
    shared={"c_bytes": c_bytes},
)