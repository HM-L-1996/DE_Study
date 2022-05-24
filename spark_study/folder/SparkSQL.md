# Spark SQL

- 목적
    - 스파크 프로그래밍 내부에서 관계형 처리를 하기 위해
    - 스키마의 정보를 이용해 자동으로 최적화하기 위해
    - 외부 데이터셋을 사용하기 쉽게 하기 위해
- DataFrame
    - 테이블 데이터셋
    - 개념적으로 RDD에 스키마가 적용된 것
    - RDD로 변환해 사용할 수 있지만 사용하지 않는걸 권장
        - DataFrame의 이점
            - MLLib이나 Spark Streaming 같은 다른 스파크 모듈들과 사용하기 편하다
            - 개발하기 편하다
            - 최적화도 알아서 된다
    - 만들기
        - RDD에서 스키마를 정의한 다음 변형
        - CSV,JSON 등의 데이터를 받아오는 것
        - Schema를 자동으로 유추해서 DataFrame 만들기
        - Schema를 사용자가 정의하기
        - DataFrame을 하나의 데이터베이스 테이블처럼 사용하려면 createOrReplaceTempView() 함수로 temporary view를 만들어줘야 한다.
- SparkSession
    - Spark Core에 SparkContext가 있다면 Spark SQL엔 SparkSession이 있다.
        - spark 세션으로 불러오는 데이터는 데이터프레임 형식
        
        ```python
        spark = SparkSession.builder.appName("test-app").getOrCreate()
        ```
        
- Datasets
    - Type이 있는 DataFrame
    - PySpark에선 크게 신경쓰지 않아도 된다.
        - Python 자체가 Strongly Type이 아니기 때문