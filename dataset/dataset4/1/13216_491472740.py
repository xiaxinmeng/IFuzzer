rc = conn.execute(
    'with c(k, v) as (select key, value + 10 from kv) '
    'update kv set value=(select v from c where k=kv.key)')