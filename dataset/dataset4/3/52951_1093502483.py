import os, shutil, user

desktop_dir = os.path.join(user.home, 'Desktop')
os.chdir(desktop_dir)

shutil.rmtree('')