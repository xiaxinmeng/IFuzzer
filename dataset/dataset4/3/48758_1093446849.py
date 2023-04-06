def whoami():
   """return a string identifying the user."""
   return (os.environ.get("USER") or os.environ.get("USERNAME") or
"unknown").replace(" ","")