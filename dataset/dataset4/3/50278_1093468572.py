def error_handle():
    try:
        print(5/0)
    except:
        error_handle()

error_handle()