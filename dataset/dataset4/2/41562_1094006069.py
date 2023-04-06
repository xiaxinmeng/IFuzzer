pycon
"""
>>> p=Meld(open('player.html','rb').read())
>>> p.StreamURL1.value
'mss://stream.url'
>>> p.StreamURL2
<PyMeld.Meld instance at 0x00B455F8>
>>> p.StreamURL2.src
'mms://stream.url'

>>> v=Video()
>>> v.stream
's'
>>> p.StreamURL1.value=v.stream
>>> p.StreamURL1.value

>>> ================================ 
RESTART 
================================
>>> 
"""
