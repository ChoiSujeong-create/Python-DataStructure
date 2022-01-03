#  LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))
import queue
data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(100)
data_queue.put(5)

# 출력 -> ['funcoding', 100, 5]
print(data_queue.queue)

# 출력 -> 5
print(data_queue.get())

# 출력 -> ['funcoding', 100]
print(data_queue.queue)

# 출력 -> 2
print(data_queue.qsize())
