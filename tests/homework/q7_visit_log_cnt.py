"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요
# Q7. 2022년 7월 12일 총 방문 횟수를 가져오는 쿼리를 작성하세요(10점)
# 아래 함수를 실행하면, int 값을 반환해야합니다.
# 리턴 타입의 예는 아래와 같습니다.
# 15

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
import psycopg

def get_total_visit_in_2022_07_12() -> int:
    with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select count(*)
                from visit_log
                where enter >= '2022-07-12' and enter < '2022-07-13'
            """)
            return cur.fetchall()