if len(mbox.list_folders()) <= 0:
  # no sub-folders, safe to delete?
  mbox.delete()