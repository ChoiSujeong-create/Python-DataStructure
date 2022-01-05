# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기
class Node:
    def __init__(self, data, next=None):  # data 만 입력시 next 초기값은 None이다.
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):  # linkedlist 구조체의 첫 머리부분
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedlist1 = NodeMgmt(0)  # linkedlist(NodeMgmt형식)의 head는 0이 됨
linkedlist1.desc()
print()
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
