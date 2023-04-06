def close():
    os.set_blocking(w, True)
    f_w.close()
threading.Thread(target=close).start()

b = f_r.read()
f_r.close()