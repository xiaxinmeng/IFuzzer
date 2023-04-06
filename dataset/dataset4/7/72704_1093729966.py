if conn.in_transaction:
    conn.commit()
conn.execute("vacuum")