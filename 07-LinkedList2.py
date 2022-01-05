# linked list로 데이터 추가하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

# 데이터 출력하기
node = head
while node:
    print(node.data, end=" ")
    node = node.next
print()
# linked list 사이에 data 추가하기
node3 = Node(1.5)
node = head
search = True

while search:
    if node.data == 1:
        search = False  # while stop
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

# print
node = head
while node:
    print(node.data, end=" ")
    node = node.next
