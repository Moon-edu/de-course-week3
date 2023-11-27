import psycopg

def get_total_visit_by_purpose() -> list:
    data = []
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("select purpose, count(*) from visit_log group by purpose;")
            data = cur.fetchall()
    return data
