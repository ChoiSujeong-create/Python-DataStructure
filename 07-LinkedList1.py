class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Node와 Node 연결하기 (포인터 활용)
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# Node 데이터 출력하기
node = node1
while node:
    print(node.data, end=" ")
    # 출력 후 다음으로 넘어가기
    node = node.next
