if makedirs("a/b", mod=0o755, exists_ok=True):
  os.chmod("a", 0o755)
  os.chmod("a/b", 0o755)
# else a and b were created with the permission 0o755