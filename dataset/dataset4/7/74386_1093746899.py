def get_size(event):
    # self.size.set(listbox_size.get(listbox_size.curselection()))
    # ____TEST____ >
    ok=True
    try:
        lb_siz_cur = listbox_size.curselection()
        lb_siz_get =  listbox_size.get(lb_siz_cur)
    except:
        ok=False
    if ok:
        self.size.set(lb_siz_get)