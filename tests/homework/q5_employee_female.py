"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요
# Q5. employee 테이블에서 성별이 Female인 직원의 나이와 직위(Position)을 가져오는 Query를 작성하세요(10점)
# 아래 함수를 실행하면, Tuple 리스트를 반환해야합니다. 결과 값의 각 레코드의 칼럼 순서는 반드시 아래의 순서로 되어야 합니다.(e.g 직위가 먼저 올 경우 오답 처리됩니다.)
# 리턴 타입의 예는 아래와 같습니다.(나이, 포지션 순)
# [(30, "position1"), (23, "position2")]

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
def find_employee_female_table() -> list:
    with psycopg.connect("dbname=postgres host=localhost user=postgres password=postgres") as conn:
        with conn.cursor() as cur:
            genders = ("Female",)
            cur.execute(f"""
                SELECT age, position
                FROM employee
                WHERE gender = %s;
                """, genders)
            results = cur.fetchall()
            print(results)

        conn.commit()