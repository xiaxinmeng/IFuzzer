try:
   ...
except Exception as e:
    try:
        ...
    finally:
         e = None
         del e