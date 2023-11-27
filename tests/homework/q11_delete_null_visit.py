import psycopg

def delete_null_visit():
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("delete from visit_log where visitor is null;")
