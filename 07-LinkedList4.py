class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
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
    # 특정 노드를 삭제

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        # head 값을 삭제할 때
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:  # 첫번째 노드가 아닌 다른 값을 삭제할 때
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


# 노드 1개 생성
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# head가 살아있음을 확인
print(linkedlist1.head)

# head 삭제
linkedlist1.delete(0)
# head를 출력해봄으로서 확인
print(linkedlist1.head)

# 다시 노드를 만들어봄
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# 여러개의 노드 추가
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()

# 노드 중 한개를 삭제함
linkedlist1.delete(4)
# 노드 삭제 확인
linkedlist1.desc()

linkedlist1.delete(9)
linkedlist1.desc()
