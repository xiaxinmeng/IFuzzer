with open(os.devnull, "wb") as null:
    proc = subprocess.Popen(..., stdout=null)