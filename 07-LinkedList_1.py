# 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고, 테스트 해보기
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

    def search_Node(self, data):
        node = self.head
        while node.next:
            if node.data == data:
                return node
            else:
                node = node.next


node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)
print(node_mgmt.search_Node(4).data)
