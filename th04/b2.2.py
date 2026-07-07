from collections import deque

q = deque()                 # deque([])

q.append('data analytics')  # deque(['data analytics'])
q.append('data structures and algorithms')
q.append('big data')
q.append('learning data analytics')

print(q)

print(q.popleft())          # data analytics
print(q.popleft())          # data structures and algorithms

print(q)