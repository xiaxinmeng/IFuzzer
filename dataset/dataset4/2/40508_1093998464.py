def fn(record): return '%s (%s)'%(record.name,record.number)

value=getattr(record,fn)