
import _codecs_jp
import gc
codec = _codecs_jp.getcodec('cp932')
# instance -> type
print(gc.get_referents(codec) == [type(codec)])
# type -> instance
print(any(ref is codec for ref in gc.get_referrers(type(codec))))
