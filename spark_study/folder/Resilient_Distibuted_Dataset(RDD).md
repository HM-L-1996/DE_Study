# Resilient Distibuted Dataset (RDD)

- 여러 분산 노드에 걸쳐서 저장
- 변경이 불가능
- 여러 개의 파티션으로 분리
- 특징
    - 데이터 추상화
        - 데이터는 클러스터에 흩어져 있지만 하나의 파일인 것 처럼 사용이 가능하다.
    - Resilient & Immutable
        - 탄력적이고 불변하는 성질이 있다.
        - Immutable
            - 데이터가 여러군데서 연산되는 중 여러 노드 중 하나가 망가진다면?
                - 데이터가 불변, 즉 Immutable 하면 문제가 일어날 때 복원이 가능해진다.
        - Resilent
            - RDD1이 변환을 거치면 RDD1이 바뀌는게 아니라 새로운 RDD2가 만들어진다.
            - 변환을 거칠때마다 연산의 기록이 남는다.(변환 과정은 하나의 비순환 그래프)
            - RDD1이 연산 중 문제가 생기면 다시 복원 후 RDD2에서 연산하면 된다.
    - Type-safe
        - 컴파일시 Type을 판별할 수 있어 문제를 일찍 발견할 수 있다.
    - Unstructured / Structered Data
    - Lazy
        - 결과가 필요할때까지 연산을 하지 않는다.
        - 연산 종류
            - 변환
            - 액션
        
        ![Untitled](Resilient_Distibuted_Dataset(RDD)/Untitled.png)
        
        - 액션을 할 때까지 변환은 실행되지 않는다. Action을 만나면 전부 실행된다.
- 장점
    - 유연하다.
    - 짧은 코드로 할 수 있는게 많다
    - 개발할 때 **무엇**보다는 **어떻게**에 대해 더 생각하게 한다.
        - Lazy 덕분에 데이터가 어떻게 변환될 지 생각하게 된다.