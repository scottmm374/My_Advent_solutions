class FileNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class SystemTree:
    def __init__( self, node=None):
        self.head = node
        self.tail = node
        # Need length?


    def __repr__(self):
        current_node = self.head
        nodes = []
        while current_node:
            if current_node is self.head:
                nodes.append(f'[HEAD:{current_node.value}]')
                current_node = current_node.next
            elif current_node is self.tail:
                nodes.append(f'[TAIL:{current_node.value}]')
                current_node = current_node.next
            else:
                nodes.append(f'[{current_node.value}]')
                current_node = current_node.next
        return "".join(nodes)


    def add_to_tail(self, value):
        if self.tail is None:
            new_node = FileNode(value)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = FileNode(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None


tree = SystemTree()
tree.add_to_tail("a")
tree.add_to_tail("b")
tree.add_to_tail("c")
tree.add_to_tail("d")
tree.add_to_tail("e")
tree.add_to_tail("f")
print(tree)