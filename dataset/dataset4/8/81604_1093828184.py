def testSomeRequest(self):

    request = {"someRequest": "request"}
    response = self.sendSearchRequest(request)
    print(response.next_page_token)