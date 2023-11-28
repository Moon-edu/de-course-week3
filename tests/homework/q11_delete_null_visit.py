"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요

Q11. visitor값이 null인 레코드를 삭제하는 로직을 작성하세요(10점)
Query의 실행 결과 데이터베이스에서 visitor가 null인 레코드가 삭제되어 검색이 되지 않아야 합니다.
Hint: delete를 사용하세요

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
def delete_null_visit():
    with psycopg.connect("dbname=postgres host=localhost user=postgres password=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                DELETE FROM visit_log
                WHERE visitor IS NULL
            """)

        conn.commit()

