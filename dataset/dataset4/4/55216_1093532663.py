class C:
    def bomb(self):
        1/0

c = C()
c.bomb()