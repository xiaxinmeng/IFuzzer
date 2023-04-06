import shlex
args = shlex.split('mpirun -np 4 myexe.x moreargs')
completed_ps = subprocess.run(args)
# now completed_ps.returncode = 1 if myexe.x moreargs fails.