# Queue()로 큐 만들기  FIFO(First-In, First-Out)
import queue
data_queue = queue.Queue()

data_queue.put("Sally starts leaning python")
data_queue.put(27)

# 출력 -> deque(['Sally starts leaning python', 27])
print(data_queue.queue)
print(data_queue.qsize())
data_queue.get()

# 출력 -> deque([27])
print(data_queue.queue)
print(data_queue.qsize())
data_queue.get()

# 출력 -> deque([])
print(data_queue.queue)
print(data_queue.qsize())
