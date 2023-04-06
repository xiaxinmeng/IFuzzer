process = subprocess.Popen(
    [
        'powershell.exe',
        script
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)