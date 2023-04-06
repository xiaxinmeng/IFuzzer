import os
import subprocess

clip_path = os.path.join(os.environ['SystemRoot'], 'System32', 'clip.exe')
p = subprocess.run('clip', executable=clip_path,
    creationflags=subprocess.DETACHED_PROCESS,
    input='spam & eggs', encoding='utf-16le')