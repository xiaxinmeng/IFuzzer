class HTTPRedirectHandler(BaseHandler):
    redirect_post_data = False
    ...
    ...
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        ...
        ...
        data = None
        if req.has_data() and self.redirect_post_data:
            data = req.get_data()
        return Request(newurl,
                       data=data,
                       headers=newheaders,
                       origin_req_host=req.get_origin_req_host(),
                       unverifiable=True)