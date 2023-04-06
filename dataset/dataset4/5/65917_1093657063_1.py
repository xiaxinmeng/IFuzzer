cursor.execute("""
    with bar as (select * from foo)
    select * from bar where id = 10
""")