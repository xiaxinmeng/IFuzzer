def deco2(f):
    return f

f = 5
f = (
     deco1(
         deco2(
             f
         )
     )
)