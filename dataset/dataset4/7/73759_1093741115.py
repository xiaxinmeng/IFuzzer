with tempfile.NamedTemporaryFile(delete=False) as f:
    try:    
        f.write(b'data')
        f.close()
        subprocess.Popen(['binutil', f.name, ...])
    finally:
        os.unlink(f.name)