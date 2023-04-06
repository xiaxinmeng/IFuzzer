def filter_with_named_tuple_reader_writer():
   accepted_rows = []
   for row in csv.NamedTupleReader(sample_data):
     if float(row.latitude) > 0.0 and float(row.longitude) > 0.0:
       accepted_rows.append(row)

   output_writer = csv.NamedTupleWriter(
       open('accepted_by_named_tuple.csv', 'w'))
   output_writer.writerows(accepted_rows)