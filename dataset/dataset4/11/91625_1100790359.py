
class A:
    def __getattr__(self, attr):
        return int(attr.removeprefix("a"))
a = A()

def f():
    y=(a.a0+a.a1+a.a2+a.a3+a.a4+a.a5+a.a6+a.a7+a.a8+a.a9+a.a10+a.a11+a.a12+a.a13+a.a14+a.a15+a.a16+a.a17+a.a18+a.a19+
    a.a20+a.a21+a.a22+a.a23+a.a24+a.a25+a.a26+a.a27+a.a28+a.a29+a.a30+a.a31+a.a32+a.a33+a.a34+a.a35+a.a36+a.a37+a.a38+a.a39+
    a.a40+a.a41+a.a42+a.a43+a.a44+a.a45+a.a46+a.a47+a.a48+a.a49+a.a50+a.a51+a.a52+a.a53+a.a54+a.a55+a.a56+a.a57+a.a58+a.a59+
    a.a60+a.a61+a.a62+a.a63+a.a64+a.a65+a.a66+a.a67+a.a68+a.a69+a.a70+a.a71+a.a72+a.a73+a.a74+a.a75+a.a76+a.a77+a.a78+a.a79+
    a.a80+a.a81+a.a82+a.a83+a.a84+a.a85+a.a86+a.a87+a.a88+a.a89+a.a90+a.a91+a.a92+a.a93+a.a94+a.a95+a.a96+a.a97+a.a98+a.a99+
    a.a100+a.a101+a.a102+a.a103+a.a104+a.a105+a.a106+a.a107+a.a108+a.a109+a.a110+a.a111+a.a112+a.a113+a.a114+a.a115+a.a116+a.a117+a.a118+a.a119+
    a.a120+a.a121+a.a122+a.a123+a.a124+a.a125+a.a126+a.a127+a.a128+a.a129+a.a130+a.a131+a.a132+a.a133+a.a134+a.a135+a.a136+a.a137+a.a138+a.a139+
    a.a140+a.a141+a.a142+a.a143+a.a144+a.a145+a.a146+a.a147+a.a148+a.a149+a.a150+a.a151+a.a152+a.a153+a.a154+a.a155+a.a156+a.a157+a.a158+a.a159+
    a.a160+a.a161+a.a162+a.a163+a.a164+a.a165+a.a166+a.a167+a.a168+a.a169+a.a170+a.a171+a.a172+a.a173+a.a174+a.a175+a.a176+a.a177+a.a178+a.a179+
    a.a180+a.a181+a.a182+a.a183+a.a184+a.a185+a.a186+a.a187+a.a188+a.a189+a.a190+a.a191+a.a192+a.a193+a.a194+a.a195+a.a196+a.a197+a.a198+a.a199+
    a.a200+a.a201+a.a202+a.a203+a.a204+a.a205+a.a206+a.a207+a.a208+a.a209+a.a210+a.a211+a.a212+a.a213+a.a214+a.a215+a.a216+a.a217+a.a218+a.a219+
    a.a220+a.a221+a.a222+a.a223+a.a224+a.a225+a.a226+a.a227+a.a228+a.a229+a.a230+a.a231+a.a232+a.a233+a.a234+a.a235+a.a236+a.a237+a.a238+a.a239+
    a.a240+a.a241+a.a242+a.a243+a.a244+a.a245+a.a246+a.a247+a.a248+a.a249+a.a250+a.a251+a.a252+a.a253+a.a254+a.a255+a.a256+a.a257+a.a258+a.a259+
    a.a260+a.a261+a.a262+a.a263+a.a264+a.a265+a.a266+a.a267+a.a268+a.a269+a.a270+a.a271+a.a272+a.a273+a.a274+a.a275+a.a276+a.a277+a.a278+a.a279+
    a.a280+a.a281+a.a282+a.a283+a.a284+a.a285+a.a286+a.a287+a.a288+a.a289+a.a290+a.a291+a.a292+a.a293+a.a294+a.a295+a.a296+a.a297+a.a298+a.a299)
    return y

for i in range(12):
    print(f())
# 44850
# 44850
# 44850
# 44850
# 44850
# 44850
# 44850
# Traceback (most recent call last):
#   File "C:\Users\sween\Source\Repos\cpython2\cpython\unpack.py", line 26, in <module>
#     print(f())
#           ^^^
#   File "C:\Users\sween\Source\Repos\cpython2\cpython\unpack.py", line 20, in f
#     a.a240+a.a241+a.a242+a.a243+a.a244+a.a245+a.a246+a.a247+a.a248+a.a249+a.a250+a.a251+a.a252+a.a253+a.a254+a.a255+a.a256+a.a257+a.a258+a.a259+
#                                                                                                              ^^^^^^
#   File "C:\Users\sween\Source\Repos\cpython2\cpython\unpack.py", line 4, in __getattr__
#     return int(attr.removeprefix("a"))
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: ''