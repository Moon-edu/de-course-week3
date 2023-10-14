"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요
Q10. Peach의 position을 Senior engineer로 수정하는 로직을 작성하세요(10점)
Query의 실행 결과 데이터베이스에서 Peach의 직위가 Senior engineer로 수정되어 있어야 합니다.

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
import psycopg
def update_peach_position():
    with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
        to_update = ("Senior engineer", "Peach")
        with conn.cursor() as cur:
            cur.execute(f""" update employee 
                                      set position = %s
                                    where name = %s """, to_update)
        conn.commit()
