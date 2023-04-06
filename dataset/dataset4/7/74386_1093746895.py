def get_style(event):
        # self.style.set(listbox_style.get(listbox_style.curselection()))
        # ____TEST____ >
        lb_sty_cur = listbox_style.curselection()
        if lb_sty_cur:
            lb_sty_get = listbox_style.get(lb_sty_cur)
            self.style.set(lb_sty_get)
        return