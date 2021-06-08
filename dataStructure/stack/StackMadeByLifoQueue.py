import queue

lifo_queue = queue.LifoQueue()
lifo_queue.put(1)
lifo_queue.put(2)
lifo_queue.put(3)

print(lifo_queue.get())
print(lifo_queue.get())
print(lifo_queue.get())
