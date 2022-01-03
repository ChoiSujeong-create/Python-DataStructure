# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]  # 추출한 데이터 삭제
    return data  # 삭제한 데이터 반환


for idx in range(10):  # 0~9를 리스트에 insert
    enqueue(idx)

# 출력 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(queue_list)
print(len(queue_list))  # list에 들어간 데이터 갯수
dequeue()  # 맨 앞에 들어있는 데이터 삭제
# 출력 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(queue_list)
