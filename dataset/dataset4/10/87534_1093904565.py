def test_return_empty_bytes(self):
    cur = self.con.cursor()
    cur.execute("select X''")
    val = cur.fetchone()[0]
    self.assertEqual(val, b'')