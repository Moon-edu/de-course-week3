import psycopg

def update_peach_position():
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("update employee set position='Senior engineer' where name='Peach';")
