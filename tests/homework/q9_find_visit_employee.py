"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요
# Q9. 2022-07-11 09:00:00 에 방문한 사람의 이름과 부서 번호, 사번(emp_id)을 가져오는 쿼리를 작성하세요(10점)
# 아래 함수를 실행하면, Tuple list값을 반환해야합니다.
# 결과 값은 아래와 같이 이름, 부서 번호, 사번 순으로 되어야 합니다.
# 리턴 타입의 예는 아래와 같습니다.
# [("name1", 3, "A00107"), ("name2", 1, "B10730")]

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
import psycopg
def get_visitor_in_2022_07_11_09_00() -> list:
    with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute(""" select ta.name, ta.department, ta.emp_id
                               from employee ta
                               join visit_log tb
                                 on ta.emp_id = tb.visitor
                              where tb.enter = '2022-07-11 09:00:00' """)

            visitor= cur.fetchall()

        conn.commit()
        return(visitor)

