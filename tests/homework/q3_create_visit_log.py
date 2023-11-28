import psycopg

def create_visit_log_table():
    with psycopg.connect('dbname = postgres host = localhost user = postgres password = postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("""
                    create table visit_log(
	                    visitor varchar(6) check(visitor ~ '^[A-Z]\d{5}$'),
	                    enter timestamp not null,
	                    out timestamp,
	                    purpose varchar(50)
                    );
                """)
        conn.commit()