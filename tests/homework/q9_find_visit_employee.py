import psycopg

def get_visitor_in_2022_07_11_09_00() -> list:
    data = []
    with psycopg.connect('dbname=postgres host=localhost user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("select employee.name, employee.department, employee.emp_id from employee join visit_log on employee.emp_id=visit_log.visitor where visit_log.enter='2022-07-11 09:00:00';")
            data = cur.fetchall()
    return data

