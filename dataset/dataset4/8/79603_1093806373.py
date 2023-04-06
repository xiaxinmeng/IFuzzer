http_connection = HTTPSConnection("localhost")
http_connection.request("POST", my_url, my_body, my_headers)