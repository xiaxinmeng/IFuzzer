
import mock


target = dict(a=1)

@mock.patch.dict('test_patch_dict.target', dict(b=2))
def test_after_patch():
	assert target == dict(a=2, b=2)

target = dict(a=2)
