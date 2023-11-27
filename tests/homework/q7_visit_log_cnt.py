import psycopg

def get_total_visit_in_2022_07_12() -> int:
    data = []
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("select count(*) from visit_log where enter>='2022-07-12' and enter<'2022-07-13';")
            data = cur.fetchone()[0]
    return data
