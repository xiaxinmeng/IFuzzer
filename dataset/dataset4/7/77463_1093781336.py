process = subprocess.Popen(
    [
        'powershell.exe',
        script
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)