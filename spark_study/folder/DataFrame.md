# DataFrame

- 관계형 데이터셋 : RDD + Relation
- RDD가 함수형 API를 가졌다면 DataFrame은 선언형 API
- 자동으로 최적화가 가능
- 타입이 없다
- 특징
    - 지연 실행
    - 분산 저장
    - Immutable
    - 열(Row) 객체가 있다
    - SQL 쿼리를 실행할 수 있다.
    - 스키마를 가질 수 있고 이를 통해 성능을 더욱 최적화할 수 있다.
    - CSV,Json,Hive 등으로 읽어오거나 변환이 가능하다.
- Operations
    - Select,Where
    - Limit
    - OrderBy
    - GroupBy
    - Join
    - Agg
        - Aggregate의 약자로, 그룹핑 후 데이터를 하나로 합치는 작업


