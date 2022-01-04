stack_list = list()


def pop():
    data = stack_list[len(stack_list)-1]
    del stack_list[len(stack_list)-1]
    return data
# stack_list[-1]
# -1 은 리스트의 맨 마지막 요소를 의미함


def push(data):
    stack_list.append(data)


for idx in range(10):
    push(idx)
print(stack_list)
print(pop())
