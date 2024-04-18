# import queue

# x = [1,2,3]
# y = queue.Queue()
# for i in range(len(x)):
#     y.put(x[i])

# while not y.empty():
#     print(y.get())
import queue
q = queue.Queue()
# q.push(1)
q.put('foo')
q.put('bar')
d = q.queue

print(q.get())
print(q.get())
print(q.get())