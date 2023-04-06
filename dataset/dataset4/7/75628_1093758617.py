proc = subprocess.Popen(proc_str,
                                    stdin=subprocess.PIPE,
                                    stderr=errPipeW,
                                    stdout=outPipeW,shell=False,
                                    universal_newlines=True)

proc.communicate(timeout=20)
os.close(outPipeW)
os.close(errPipeW)