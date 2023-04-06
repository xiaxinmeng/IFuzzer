from http.client import OK, HTTPConnection
import unittest

class TestProxy(unittest.TestCase):
    def test_proxy_tunnel_success(self):
        con = HTTPConnection('localhost', 4242)
        con.set_tunnel('www.example.com')
        con.request('GET', 'http://www.example.com')
        resp = con.getresponse()
        self.assertEqual(resp.code, 200)
        data = resp.read()
        con.close()

    def test_proxy_tunnel_failure(self):
        con = HTTPConnection('localhost', 4242)
        con.set_tunnel('www.example.com')
        con.request('GET', '/')
        resp = con.getresponse()
        self.assertEqual(resp.code, 200) # FAILS
        con.close()

if __name__ == '__main__':
    unittest.main()