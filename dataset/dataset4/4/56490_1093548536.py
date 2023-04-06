def fsdecode(filename):
   if isinstance(filename, bytes):
       return codecs.code_page_decode(codecs.CP_ACP, filename, flags=0)
   elif isinstance(filename, str):
       return filename
   else:
       raise TypeError()