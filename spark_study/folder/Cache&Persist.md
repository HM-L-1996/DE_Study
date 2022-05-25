# Cache & Persist

- Transform
    - 결과값으로 새로운 RDD를 반환
    - 지연 실행 - Lazy Execution
        - 메모리를 최대한 활용할 수 있다. (디스크,네트워크 연산을 최소화 할 수 있다)
        - 데이터를 다루는 task는 반복되는 경우가 많다
            - 머신러닝 학습
            - 반복을 할 때 생기는 비효율
                - 비효율적
                    - Task → Disk → Task → Disk
                - In-memory 방식으로
                    - Task → Task
                    - 조건 : 어떤 데이터를 메모리에 남겨야 할지 알아야 가능하다.
- Transformations는 지연 실행되기 때문에 메모리에 저장해둘 수 있다.
    - 데이터를 메모리에 남겨두고 싶을 때 사용할 수 있는 함수
        - Cache()
            - 디폴트 Storage Level 사용
            - RDD : MEMORY_ONLY
            - DF : MEMORY_AND_DISK
            - Regression에서의 사용방법
                
                ```python
                points = sc.textfile("...").map(parsePoint).cache
                # points를 한번 로딩한 다음에 메모리에 저장해두고 반복 연산을 실행
                for i in range(ITERATIONS):
                	gradient = points.map(gredient_descent)
                									 .reduce(lambda x,y : (x+y)/n)
                	w -= gradient * learning_rate
                ```
                
        - Persist()
            - Storage Level을 사용자가 원하는대로 지정 가능
            
            ```python
            categoryReviews = filtered_lines.map(parse).persist()
            
            result1 = categoryReviews.take(10)
            result2 = categoryReviews.mapValues(lambda x:(x,1).collect())
            ```
            
        - 여러 종류의 Storage Level
            
            
            | Storage Level | Meaning |
            | --- | --- |
            | MEMORY_ONLY | 메모리에만 데이터를 저장 |
            | MEMORY_AND_DISK | 메모리와 디스크 동시에 데이터를 저장 (메모리에 데이터가 없을 경우 디스크까지) |
            | MEMORY_ONLY_SER | 구조화된 데이터를 Serialize(직렬화)- 용량을 아끼기 위해 사용하지만 데이터를 읽을 때 DeSerailize를 해야 하기 때문에 TradeOff가 일어남 |
            | MEMORY_AND_DISK_SER | 위와 동일 |
            | DISK_ONLY | 디스크에만 데이터를 저장 |
- Actions
    - 결과값을 연산하여 출력하거나 저장
    - 즉시 실행 - Eager Execution
