def task():
    dirname = tempfile.mkdtemp()
    f_w =  open(os.path.join(dirname, "stdout.txt"), "w")
    e_w =  open(os.path.join(dirname, "stderr.txt"), "w")

    with subprocess.Popen("dir", shell=True, stdout=f_w, stderr=e_w) as p:
        pass

    f_w.close()
    e_w.close()

    shutil.rmtree(dirname)