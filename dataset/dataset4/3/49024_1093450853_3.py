def close_db(dbenv, db):
    try:
        if db:
            db.close()
        if dbenv:
            db_env.close()
    except Exception:
        log.rcpt.exception('closing db')
    else:
        log.rcpt.info('db closed')