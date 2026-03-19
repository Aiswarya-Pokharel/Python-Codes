## TUPLES
location = (27.7172, 85.3240)
print("Latitude:", location[0])
print("Longitude:", location[1])


## DICTIONARY
student = {
  "name": "Aiswarya",
  "address": "Jhapa",
  "age": 20 
}
print(student["name"],student["address"],student["age"])


##SET
visitors = {"Ram", "Shyam", "Hari", "Ram"}
print(visitors)


##STACK
stack = []
stack.append("Type A")
stack.append("Type B")
stack.append("Delete Word")
print("Actions:", stack)
undo = stack.pop()
print("Undo:", undo)
print("Remaining:", stack)


##QUEUE
from collections import deque
queue= deque()
queue.append("Ram")
queue.append("Hari")
queue.append("Sita")

print("Queue: ",queue)
served = queue.popleft()
print("Served:", served)
print("Remaining:", queue)
