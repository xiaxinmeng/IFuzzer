def list_supported_codecs():
  for codec in codecs.registered_codecs():
    print(codec.name)