con = sqlite3.connect('existing_db.db')
with sqlite3.connect('backup.db') as bck:
    con.backup(bck, pages=1, progress=progress)