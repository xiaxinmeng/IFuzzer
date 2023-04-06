import sre as re

re_fmt = re.compile(
                        "("
                            "%"
                            "(?P<precision>"
                                "\d+"
                                "(?:"
                                    "[.]"
                                    "\d+"
                                ")"
                            ")?"
                            "(?:"
                                "[(]"
                                "(?P<key>"
                                    "[^)]*"
                                ")?"
                                "[)]"
                            ")?"
                            "(?P<c>[a-z])"
                        ")"
                    )