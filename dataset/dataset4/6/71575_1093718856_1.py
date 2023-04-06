def VarChanged_spaceNum(self, *params):
    value = self.spaceNum.get()
    self.AddChangedItem('main', 'Indent', 'num-spaces', value)