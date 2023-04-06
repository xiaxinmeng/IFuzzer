self.font_bold = tracers.add(parent, BooleanVar, 
                         callback=self.var_changed_font, 
                         config=('main', 'EditorWindow', 'font-bold'))
self.space_num = tracers.add(parent, IntVar, 
                         callback=default, 
                         config=('main', 'Indent', 'num-spaces'))