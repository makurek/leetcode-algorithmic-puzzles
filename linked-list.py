
class Node:
    def __init__(self, next = None, content = None):
        self.next = next
        self.content = content

    def addNode(self, node):
        self.next = node

head = None

for i in range (0,10):
    inp = input("Please enter a number: ")
    if i == 0:
        n = Node(next = None, content = inp)
        previous = n
        head = n
    else:
        n = Node(next = None, content = inp)
        previous.next = n
        previous = n

current_node = head

while True:
    print(current_node.content)
    if (current_node.next == None):
        break
    else:
        current_node = current_node.next






