def ls(dir, select='*', reject='.*'):
    return (p for p in dir.glob(select) if not p.match(reject))