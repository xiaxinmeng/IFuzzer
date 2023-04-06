class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path =='/':
            f = self.home_head()
        elif self.path in self.custom_paths:
            f = self.special_head()
        else:
            f = self.send_head()
        # ...
        # Standard Code