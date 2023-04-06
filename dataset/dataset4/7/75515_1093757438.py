import select

p = select.poll()
p.poll(-100)
#