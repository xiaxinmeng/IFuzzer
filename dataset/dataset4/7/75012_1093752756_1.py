connstream = ssl.wrap_socket(newsocket, server_side=True, certfile=self.certfile, keyfile=self.keyfile)

pipe = multiprocessing.Pipe()
proc = multiprocessing.Process(target=proc_run, args=(pipe[0],), daemon=False)
proc.start()