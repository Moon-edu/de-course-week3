import psycopg

def find_employee_female_table() -> list:
    data = []
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("select age,position from employee where gender='Female';")
            data = cur.fetchall()
    return data