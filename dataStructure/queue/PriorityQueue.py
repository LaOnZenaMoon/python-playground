import queue

priority_queue = queue.PriorityQueue()
priority_queue.put((10, "A"))
priority_queue.put((1, "B"))
priority_queue.put((5, "C"))
priority_queue.put((12, "D"))

print(priority_queue.qsize())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.qsize())
