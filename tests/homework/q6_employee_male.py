import psycopg

def find_employee_male_table() -> list:
    data = []
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("select name, age, position from employee where gender='Male' order by age desc;")
            data = cur.fetchall()
    return data