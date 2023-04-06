class BadTest(unittest.TestCase):
    def test_bad(self):
        class C:
            def __init__(self):
                pass

        cls_id = hex(id(C))
        tp_version_tag_before = C.v
        x = C()
        tp_version_tag_after = C.v
        print(f'C ID: {cls_id}, before: {tp_version_tag_before} after: {tp_version_tag_after}')