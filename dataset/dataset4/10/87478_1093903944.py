def get_preferred_schemes():
    if os.name == "nt":
        return {
            "prefix": "nt",
            "home": "posix_home",
            "user": "nt_user",
        }
    return {
        "prefix": "posix_prefix",
        "home": "posix_home",
        "user": "posix_user",
    }