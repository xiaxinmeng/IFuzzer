def f():
    try:
        if something(): return
    finally:
        try:
            if something(): return
        finally:
            try:
                if something(): return
            finally:
                try:
                    if something(): return
                finally:
                    try:
                        if something(): return
                    finally:
                        do_cleanup()


import dis
dis.dis(f)