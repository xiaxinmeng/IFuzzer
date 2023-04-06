def f():
    while True:
        try:
            if something(): break
            elif something_else(): continue
            elif yet_something_else(): return
        finally:
            try:
                if something(): break
                elif something_else(): continue
                elif yet_something_else(): return
            finally:
                try:
                    if something(): break
                    elif something_else(): continue
                    elif yet_something_else(): return
                finally:
                    try:
                        if something(): break
                        elif something_else(): continue
                        elif yet_something_else(): return
                    finally:
                        do_cleanup()