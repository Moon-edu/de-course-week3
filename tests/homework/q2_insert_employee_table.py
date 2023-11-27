import psycopg

def insert_employee_table():
    with psycopg.connect('dbname = postgres host = localhost user = postgres password = postgres') as conn:
        with conn.cursor() as cur:
            data = [
                ('A00001', 'Male', 'Moon', '10-199, Gang-nam, Seoul', 1, 'C00001', 30, 'Senior engineer'),
                ('B00100', 'Female', 'Sun', '587/8, Gwan-ak, Seoul', 2, 'B00102', 25, 'Associate marketer'),
                ('A08771', 'Others', 'Peach', '203-3, Guro, Seoul', 1, 'C00001', 26, 'Junior engineer'),
                ('C00129', 'Male', 'Alex', '20-331, Bundang, Gyonggi', 3, 'C00002', 40, 'Director'),
                ('C00001', 'Male', 'Lion', '53-3, Namyang-ju, Gyonghi', 1, 'C00000', 55, 'CTO'),
                ('C00002', 'Others', 'Cindy', '100, Jong-ro, Seoul', 3, 'C00000', 52, 'Director'),
                ('B00102', 'Female', 'Ran', '290-10, Gwanghwamun, Seoul', 2, 'C00000', 45, 'Director'),
                ('C00000', 'Male', 'K', '1010, Sung-soo, Seoul', None, None, 51, 'CEO')
            ]
            cur.executemany(f"insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)", data)
        conn.commit()