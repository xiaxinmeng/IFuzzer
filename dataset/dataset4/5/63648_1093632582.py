import cStringIO, csv

sio=cStringIO.StringIO()
writer=csv.DictWriter(sio, ["foo", "bar"])
writer.writerow({1:"hello", 2:"world"})