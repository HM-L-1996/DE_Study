# Cluster Topology

- Spark는 Master Worker Topology로 구성
    - 항상 데이터가 여러곳에 분산되어 있다는 것
    - 같은 연산이어도 여러 노드에 걸쳐서 실행된다는 점
    - 구조
        
        ![Untitled](Untitled%201.png)
        
        - Driver Program - Master
            - Spark Context가 있는 곳으로 Spark Context는 새로운 RDD를 생성
            - 개발자나 유저가 프로그램과 상호작용을 하는 노드(작업들을 조작)이고 실제 작업을 수행하는 곳은 Worker Node다.
            - Transformation과 Action을 저장해두거나 Worker Node들에게 전송
        - Cluster Manager
            - 수행되는 작업들에 대한 Scheduling과 Cluster 전반에 대한 자원 관리
        - Worker Node
            - Executor가 연산을 수행하고 데이터를 저장(Task)
            - Driver Program에 연산결과를 전송
            - 연산을 하면서 필요한 저장공간(Cache)을 제공
        - RDD 수행
        
        ```python
        #1
        RDD.foreach(lambda x: print(x)) # Driver Program에서는 아무런 결과도 나오지 않음 
        # foreach는 Action이기 때문에 executor에서 바로 실행되기 때문
        #2
        foods = sc.parallelize(["짜장면", "마라탕",...])
        three = foods.take(3) # (3)라는 결과값은 Driver Program에 저장되어 있음
        # 일반적으로 Action은 Driver Program이 Worker Node로부터 데이터를 받는 것 까지 포함
        # Executor에게 take 함수를 수행하라고 명령하고 그 결과를 Driver Node에게 돌려주라고 요청하게 됨
        ```