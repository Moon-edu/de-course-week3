"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요.
# Q8. 방문 목적별 총 방문 횟수를 가져오는 쿼리를 작성하세요(10점)
# 아래 함수를 실행하면, Tuple list 값을 반환해야합니다.
# 리턴 타입의 예는 아래와 같습니다.
# [("work", 10), ("no_reason", 20), ("meeting", 1)]
# 결과 값 리스트의 순서는 어떤 순서로 되더라도 상관없지만, 각 레코드의 칼럼순서는 방문 목적, 횟수 순서로 되어야합니다.

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
import psycopg
def get_total_visit_by_purpose() -> list:
    with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute("""  select purpose, count(*)
                               from visit_log
                              group by purpose""")
            cnt = cur.fetchone()
        conn.commit()
        return(cnt)


