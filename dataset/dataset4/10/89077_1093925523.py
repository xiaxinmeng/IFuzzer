def good():
    class C:
        def __init__(self):  # Just to force `tp_version_tag` to update
            pass
    cls_id = hex(id(C))
    tp_version_tag_before = C.v   # v is tp_version_tag of C, exposed to Python
    x = C()                       # tp_new requires a _PyType_Lookup for `__init__`, updating `tp_version_tag`
    tp_version_tag_after = C.v
    print(f'C ID: {cls_id}, before: {tp_version_tag_before} after: {tp_version_tag_after}')

for _ in range(100):
    good()