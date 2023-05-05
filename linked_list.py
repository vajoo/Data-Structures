class Node:
    data:int = None
    next_node:int = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
    
class LinkedList:
    head = None

    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)
    
    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return current
            else:
                current = current.next_node
        return None
        
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


linked_list = LinkedList()
linked_list.add(20)
linked_list.add(156)
linked_list.add(5)
print(linked_list.size())
print(linked_list)
print(linked_list.search(156))