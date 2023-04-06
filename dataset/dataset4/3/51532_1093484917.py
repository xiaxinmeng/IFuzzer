if site.ENABLE_USER_SITE and not os.path.isdir(site.USER_SITE):
    # need to add user site directory for tests
    os.makedirs(site.USER_SITE)
    site.addsitedir(site.USER_SITE)