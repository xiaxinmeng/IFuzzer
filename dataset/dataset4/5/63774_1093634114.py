def task():
    dirname = tempfile.mkdtemp()
    f_w =  open(os.path.join(dirname, "stdout.txt"), "w")
    f_r = open(os.path.join(dirname, "stdout.txt"), "r")
    e_w =  open(os.path.join(dirname, "stderr.txt"), "w")
    e_r = open(os.path.join(dirname, "stderr.txt"), "r")

    with subprocess.Popen("dir", shell=True, stdout=f_w, stderr=e_w) as p:
        pass

    f_w.close()
    f_r.close()
    e_w.close()
    e_r.close()

    shutil.rmtree(dirname)