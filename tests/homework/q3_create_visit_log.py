"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요.
이 파일을 제대로 작성하지 않거나, 오답일 경우 자동으로 Q4, Q7, Q8, Q9, Q12이 오답 처리됩니다.
Q3. 아래 함수를 실행하면, 데이터베이스에 visit_log 테이블이 정의되어야 하며 요구사항을 준수하는 적절한 칼럼 타입과 제약사항이 설정되어야 합니다.

1. visitor는 null값이 허용되며, null일 경우 직원이 아닌 외부 손님으로 간주됩니다. 직원일 경우 직원의 ID가 기록됩니다
2. enter, out 는 출입 시간을 기록하는 데이터로 enter는 null이 될 수 없고, out은 null이 될 수 있습니다.
3. purpose는 최대 50자까지 허용되며, null값이 허용됩니다.

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""
import psycopg
def create_visit_log_table():
    with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute("""
              create table visit_log (
                   visitor varchar(6) 
                 , enter   timestamp  not null 
                 , out     timestamp 
                 , purpose varchar(50) )
                """)
        conn.commit()


