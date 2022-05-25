# airflow

- Airflow 정리
    
    에어비앤비에서 개발한 워크플로우 스케줄링, 모니터링 플랫폼
    
    - Crontab과 같은 스크립트로 워크플로우를 관리할때의 문제점
        - 실패 복구 - 언제 어떻게 다시 실행할 것인가? Backfill?
        - 모니터링 - 잘 돌아가고 있는지 어떻게 확인하기 힘들다
        - 의존성 관리 - 데이터 파이프라인간 의존성이 있는 경우 상위 데이터 파이프라인이 잘 돌아가고 있는지 파악이 힘들다
        - 확장성 - 중앙화해서 관리하는 툴이 없기 때문에 분산된 환경에서 파이프라인들을 관리하기 힘들다
        - 배포 - 새로운 워크플로우를 배포하기 힘들다
    - Airflow - 워크플로우를 작성하고 스케줄링하고 모니터링하는 작업을 프로그래밍 할 수 있게 해주는 플랫폼
        - 파이썬으로 쉬운 프로그래밍이 가능
        - 분산된 환경에서 확장성이 있음
        - 웹 대시보드
        - 커스터마이징 가능
        - 구성
            - 웹 서버 - 웹 대시보드 UI
            - 스케줄러 - 워크플로우가 언제 실행되는지 관리
            - Metastore - 메타데이터 관리
            - Executor - Task가 어떻게 실행되는지 정의
            - Worker - Task를 실행하는 프로세스
        - 워크플로우
            - 의존성으로 연결된 작업(Task)들의 집합
                - DAG(Directed Acyclic Graph)
        - Operator : 작업을 정의하는데 사용
            - Action Operator : 실제 연산을 수행
            - Transfer Operator : 데이터를 옮김
            - Sensor Operators : Task를 언제 실행시킬지 (트리거를 기다림)
            - Task : Operator Instance
                - Operator를 실행시키면 Task가 된다.
        - Airflow의 구조
            - One Node Architecture
                
                ![Untitled](ImageUntitled.png)
                
                - Metastore가 DAG에 대한 정보를 담고 있어 Web Server와 Scheduler가 해당 정보를 읽어오고 Executor로 정보를 보내서 실행시킴
                - 실행된 Task Instance는 Metastore로 보내져서 상태를 업데이트함
                - 업데이트된 상태를 Web Server와 Scheduler가 읽어와서 Task 완료 여부를 확인함
                - **Executor 안에 Queue가 존재 - Task의 순서를 정함**
            - Multi-Node Architecture
                
                ![Untitled](ImageUntitled%201.png)
                
                - **Executor 바깥에 Queue가 존재**
                    - Queue 역할 - Celery Broker
            - 동작 방식
                1. DAG를 작성하여 Workflow를 만든다. DAG는 Task로 구성되어 있다.
                2. Task는 Operator가 인스턴스화 된 것
                3. DAG를 실행시킬 때 Scheduler는 DagRun 오브젝트를 만든다 - DagRun : 사용자가 작성한 DAG의 인스턴스
                4. DagRun 오브젝트는 Task Instance를 만든다
                5. Worker가 Task를 수행 후 DagRun의 상태를 “완료”로 바꿔놓는다
    - SparkOperator - airflow에서 spark-submit만 해주고 모니터링만 함 (heavy한 작업은 spark에게 넘김)
        - Connection 추가 - local 환경/standalone
            
            ![Untitled](ImageUntitled%202.png)
            
            ```python
            #pip3 install apache-airflow-providers-apache-spark
            submit_job = SparkSubmitOperator(
                    application="/Users/ihyeonmin/Desktop/study/data-engineering/01-spark/count_trips_sql.py",
                    task_id="submit_job",
                    conn_id="spark_local"
                )
            ```