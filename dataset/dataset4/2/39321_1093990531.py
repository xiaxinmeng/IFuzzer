import robotparser   
def prompt_user_passwd(self, host, realm):
    return None, None
robotparser.URLopener.prompt_user_passwd = prompt_user_passwd    # temp patch