import io, os
i, o = os.pipe()
piperead = io.open(i,'rb',buffering=0)
p = subprocess.Popen(..., stdout=o)