def testWithTimeoutTriggeredSend(self):
        conn = self.accept_conn()
        conn.recv(88192)
+        time.sleep(1)