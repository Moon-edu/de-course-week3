import psycopg

with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:


    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE TEST (
                emp_id varchar(6) primary key,
                Gender varchar(10) not null check(Gender in ('Male', 'Female', 'Others')),
                name VARCHAR(20) NOT NULL,
                address VARCHAR(100),
                department INT CHECK(department < 100),
                manager VARCHAR(6),
                age INT CHECK(age < 200) NOT NULL,
                Position VARCHAR(30)
                )
            """)

        conn.commit()

if __name__ == "__main__":
    pass