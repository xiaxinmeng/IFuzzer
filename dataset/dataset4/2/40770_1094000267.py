if self.context_use_ps1:
    last_line_of_prompt = sys.ps1.split('\n')[-1]
else:
    last_line_of_prompt = '>>> '