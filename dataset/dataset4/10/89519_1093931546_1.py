Trig().const             # calls TrigConst.__get__
Trig().const = math.tau  # calls TrigConst.__set__
Trig.const               # calls TrigConst.__get__
Trig.const = math.pi     # overwrites TrigConst attribute with float.