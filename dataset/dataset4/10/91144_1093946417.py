
import subprocess
import sys
cmd = rf'''{sys.executable} -c "print('\u042f')"'''

print('case 1')
stdout, stderr =  subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=None).communicate()
print('case 2')
stdout, stderr =  subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
print(stderr)
