

#FIFo -> First in - First Out

#A large number of items in this list. Everty time we remove an item from the beginning of this list, all the other items need to be shifted to left.

#We can use deque object.



from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
