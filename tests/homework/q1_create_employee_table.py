import psycopg

def create_employee_table():
    with psycopg.connect('dbname = postgres host = localhost user = postgres password = postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("""
                create table employee(
	                emp_id varchar(6) unique not null check(emp_id ~ '^[A-Z]\d{5}$'),
	                gender varchar(6) not null check (gender in ('Male', 'Female', 'Others')),
	                name varchar(20) not null check(name ~ '^[a-zA-Z]+$'),
	                address varchar(100) check(address ~ '^[a-zA-Z0-9,\-\/ ]+$'),
	                department int check (department < 100),
	                manager varchar(6) check(manager ~ '^[A-Z]\d{5}$'),
	                age int not null check (age < 200),
	                position varchar(30)
	            );
            """)
        conn.commit()