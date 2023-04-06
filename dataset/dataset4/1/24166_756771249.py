
import _codecs_jp
import gc
codec = _codecs_jp.getcodec('cp932')
print(gc.get_referents(codec))
