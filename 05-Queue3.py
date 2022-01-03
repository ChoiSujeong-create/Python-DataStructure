# PriorityQueue()로 큐 만들기
# 데이터마다 우선순위를 넣어 우선순위가 높은 순으로 출력되는 형식을 가진 큐
# (우선순위, 데이터)형식의 튜플로 넣어야 한다
import queue
data_queue = queue.PriorityQueue()

data_queue.put((1, "Sally"))
data_queue.put((10, 10))
data_queue.put((7, "Korea"))

# print -> [(1, 'Sally'), (10, 10), (7, 'Korea')]
print(data_queue.queue)
# print -> (1, 'Sally')
print(data_queue.get())
# print -> [(7, 'Korea'), (10, 10)]
print(data_queue.queue)
