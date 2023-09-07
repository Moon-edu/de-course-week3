import psycopg

students = [
    ("현공부", "01033201238", 21, "영어2"),
    ("오선생", "01029083072", 27, "수학2"),
    ("구영호", "01029091234", 27, "체육1"),
    ("서강일", "01029765432", 21, "국어1")

]


class_ = [
    ("물리1", "박물리", 3),
    ("수학1", "박수학", 20),
    ("영어2", "홍영어", 100)
]

with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        for s in students:
            cur.execute(f"""
                INSERT INTO student(name, phone, age, class) 
                VALUES(%s, %s, %s, %s)
            """, s)

        for c in class_:
            cur.execute(f"""
                INSERT INTO class
                VALUES(%s, %s, %s)
            """, c)

    conn.commit()

if __name__ == "__main__":
    pass
