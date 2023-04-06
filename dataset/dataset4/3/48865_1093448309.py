src1 = db_query(query_1)
src2 = db_query(query_2)
results = deduped(src1 + src2, key=lambda x: x.field2)