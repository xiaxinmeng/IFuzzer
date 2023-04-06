result = pool.map_async(process_employee, gen_emps, chunksize=1)
while not result.ready():
   left = result._number_left