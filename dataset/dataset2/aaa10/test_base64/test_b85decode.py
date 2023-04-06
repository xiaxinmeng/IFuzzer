import unittest
import base64
import binascii
import os
from array import array
from test.support import os_helper
from test.support import script_helper
from io import BytesIO, StringIO
from io import BytesIO, StringIO
import test_base64

def test_b85decode():
    eq = BaseXYTestCase.assertEqual
    tests = {b'': b'', b'cXxL#aCvlSZ*DGca%T': b'www.python.org', b'009C61O)~M2nh-c3=Iws5D^j+6crX17#SKH9337XAR!_nBqb&%C@Cr{EG;fCFflSSG&MFiI5|2yJUu=?KtV!7L`6nNNJ&adOifNtP*GA-R8>}2SXo+ITwPvYU}0ioWMyV&XlZI|Y;A6DaB*^Tbai%jczJqze0_d@fPsR8goTEOh>41ejE#<ukdcy;l$Dm3n3<ZJoSmMZprN9pq@|{(sHv)}tgWuEu(7hUw6(UkxVgH!yuH4^z`?@9#Kp$P$jQpf%+1cv(9zP<)YaD4*xB0K+}+;a;Njxq<mKk)=;`X~?CtLF@bU8V^!4`l`1$(#{Qdp': bytes(range(255)), b'VPa!sWoBn+X=-b1ZEkOHadLBXb#`}nd3r%YLqtVJM@UIZOH55pPf$@(Q&d$}S6EqEFflSSG&MFiI5{CeBQRbjDkv#CIy^osE+AW7dwl': b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}', b'Zf_uPVPs@!Zf7no': b'no padding..', b'dS!BNAY*TBaB^jHb7^mG00000': b'zero compression\x00\x00\x00\x00', b'dS!BNAY*TBaB^jHb7^mG0000': b'zero compression\x00\x00\x00', b'LT`0$WMOi7IsgCw00': b'Boundary:\x00\x00\x00\x00', b'Q*dEpWgug3ZE$irARr(h': b'Space compr:    ', b'{{': b'\xff', b'|Nj': b'\xff' * 2, b'|Ns9': b'\xff' * 3, b'|NsC0': b'\xff' * 4}
    for (data, res) in tests.items():
        eq(base64.b85decode(data), res)
        eq(base64.b85decode(data.decode('ascii')), res)
    BaseXYTestCase.check_other_types(base64.b85decode, b'cXxL#aCvlSZ*DGca%T', b'www.python.org')

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b85decode()
