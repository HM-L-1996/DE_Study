# History

- Spark 1.0
    - RDD를 이용한 인메모리 처리 방식
    - DataFrame(V1.3)
    - Project Tungsten - 엔진 업그레이드로 메모리와 CPU 효율 최적화
        - `Project Tunsten`이란?
            - Tungsten은 Apache Spark의 실행 엔진에 변경 사항을 적용하여 메모리 및 CPU를 Spark 애플리케이션에 적합하게 효율성을 개선하는 데 중점을 두어 성능을 최신 하드웨어 한도에 더 가깝게 밀어붙이고자 추진한 엄브렐라 프로젝트의 코드명
- Spark 2.0
    - 단순화되고 성능이 개선됨
    - Structured Streaming
    - DataSet 이라는 DataFrame의 확장형 자료구조 등장
    - Catalyst Optimizer 프로젝트 - 언어에 상관없이 동일한 성능을 보장
        - `Catalyst Optimize`란?
            
            DataFrame DSL과 SQL 표현식을 하위 레벨의 RDD 연산으로 변환
            
        - Scala, Java, Python, R
- Spark 3.0
    - MLlib 기능 추가
    - Spark SQL 기능 추가
    - Spark 2.4보다 약 2배 빨라짐
        - Adaptive execution
            - 동적 셔플 파티션 통합 Dynamically coalescing shuffle partitions
                - Adaptive execution 는 셔플 통계를 보고, 런타임에 많은 수의 작은(small size) 셔플 파티션들을 합쳐 하나의 큰 파티션으로 뭉쳐주는 기능을 제공
            - 동적 전환 조인 전략 Dynamically switching join strategies
                - 한 차례 셔플이 끝난 뒤 Reoptimization 을 할 때,조인 전략이 바뀌어 더 높은 성능을 낸다는 결론이 나오면 조인 전략이 바뀐다.
                - ex) 어떤 조인에서 `브로드캐스트 해시 조인` (셔플을 사용하지 않음)으로 조인 전략이 바뀐다. - 네트워크 트래픽을 줄이는 등의 이점
            - 스큐(skew) 조인을 동적으로 최적화 Dynamically optimizing skew joins
                - skew
                    
                    파티션 하나에 데이터가 몰려있는 상황을 skew 되었다(데이터가 쏠려있다)라고 한다.
                    
                - Adaptive execution 는 skew 데이터를 감지하고, skew 데이터를 더 작은 하위 파티션으로 나눈다.
        - Dynamic partition pruning
            - Pruning
                
                내가 필요로 하지 않는 데이터를 읽지 않도록 피하는 것
                
            - full scan 을 피하기 위해 내가 필요한 데이터만 골라서 적용(읽기)하는 것.
            - star schema queries 을 위해 중요하다고 함
    - PySpark 사용성 개선
    - 딥러닝 지원 강화
        - GPU 노드 지원
        - 머신러닝 프레임워크와 연계 가능
    - GraphX - 분산 그래프 연산
        - `GraphX`란
            
            스파크의 서브 모듈로 대용량 데이터의 분산 및 병렬 그래프 처리를 지원
            
        - 추천,피드 관련 프로젝트에 이용 가능
    - Python 2 지원이 끊김
    - 쿠버네티스 지원 강화
- Spark 기능
    - Spark Core
    - Spark SQL
    - Spark Streaming
    - MLlib
    - GraphX