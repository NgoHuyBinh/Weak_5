from queue import Queue

q = Queue(maxsize=5)

print(q.qsize())

q.put('data analytics')            # ??
q.put('data structures and algorithms')
q.put('big data')
q.put('learning data analytics')

print(q.qsize())

print(q.get())                     # ??
print(q.get())