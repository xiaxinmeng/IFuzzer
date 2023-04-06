from mpi4py import MPI
from pathlib import Path
import tempfile

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

with tempfile.TemporaryDirectory() as tmp_dir:

    tmp_dir = comm.bcast(tmp_dir, root=0)
    p = Path(tmp_dir) / 'a' / 'b'
    comm.barrier()
    p.mkdir(parents=True, exist_ok=True)