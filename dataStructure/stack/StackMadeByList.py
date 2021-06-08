stack_list = list()

stack_list.append(1)
stack_list.append(2)
stack_list.append(3)
stack_list.append(4)

print(stack_list.pop())
print(stack_list.pop())
print(stack_list.pop())
print(stack_list.pop())

stack_list2 = list()

def push(data):
    stack_list2.append(data)

def pop():
    data = stack_list2[-1]
    del stack_list2[-1]
    return data

push(10)
push(20)
push(30)
push(40)

print(pop())
print(pop())
print(pop())
print(pop())