import queue

lifo_queue = queue.LifoQueue()
lifo_queue.put(2)
lifo_queue.put("star")
lifo_queue.put("coding")

print(lifo_queue.qsize())
print(lifo_queue.get())
print(lifo_queue.get())
print(lifo_queue.qsize())
