collapsed_path = _url_collapse_path(self.path)
for head in self.cgi_directories:
    if head==collapsed_path:
        self.cgi_info = (head,'')
        return True
    elif collapsed_path.startswith(head) \
        and collapsed_path[len(head)]=='/':
            self.cgi_info = head, collapsed_path[len(head)+1:]
            return True
return False