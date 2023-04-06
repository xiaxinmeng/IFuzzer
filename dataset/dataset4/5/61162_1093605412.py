with connection:   # outer transaction

    with connection:   # inner transaction
        do_X_in_db()

    do_Y_in_db()