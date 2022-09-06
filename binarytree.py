from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        #child nodes
        self.right=None
        self.left=None

def BreadthFirstPrints(root):
    #queue with root node
    queue=deque([root])
    while queue:
        #pop the leftmost element of the queue
        curr=queue.popleft()
        print(curr.value)
        #check if the node has children nodes
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right) 

def bfs(root,target):
    #queue with root node
    queue=deque([root])
    while queue:
        #pop the leftmost element of the queue
        curr=queue.popleft()
        if (curr.value == target):
            return True
        #check if the node has children nodes
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right) 
    return False


a=Node(1)
b =Node(2)
c=Node(3)
d=Node(4)
e=Node(5)  
f=Node(6)    


#         a
#       /   \
#      b     c   
#    /   \    \
#   d     e    f

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

BreadthFirstPrints(a)
print(bfs(a,1))
