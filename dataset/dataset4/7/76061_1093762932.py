import subprocess
def run_cmd(cmd):
   print("run_cmd cmd:", cmd)
   # MUST explicitly ask for stdout, stderr. timeout is in seconds
   p1 = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
   # print("run_cmd p1:", p1, type(p1))
   print("run_cmd p1.stdout:", p1.stdout, type(p1.stdout), p1.stdout.decode("utf-8"))
   print("run_cmd p1.stderr:", p1.stderr, type(p1.stderr), p1.stderr.decode("utf-8"))
   print("run_cmd p1.returncode:", p1.returncode, type(p1.returncode))

cmd = "gnuplot.exe "+self+"_candles.gnu"
run_cmd(cmd)