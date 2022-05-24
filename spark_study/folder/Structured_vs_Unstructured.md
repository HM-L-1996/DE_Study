# Structured vs Unstructured

- Spark는 데이터가 구조화되어 있다면 퍼포먼스 최적화가 가능하다.
- Structured Data vs RDD
    - RDD
        - 데이터의 구조를 모르기 때문에 데이터를 다루는 것을 개발자에게 의존
        - Map, flatMap, filter 등을 통해 유저가 만든 function을 수행
    - Structured Data
        - 데이터의 구조를 이미 알고있으므로 어떤 태스크를 수행할 것인지 정의만 하면 됨
        - 최적화도 자동으로 할 수 있음
        - SparkSQL을 사용해 구조화된 데이터를 다룰 수 있게 해준다.