class Node:
    def __init__(self, name, size=None, total_size = [] ,prev=None, next=None):
        self.name = name
        self.prev = prev
        self.next = next
        self.size = size
        self.total_size = total_size


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
                nodes.append(f'[HEAD:{current_node.name}]')
                current_node = current_node.next
            elif current_node is self.tail:
                nodes.append(f'[TAIL:{current_node.name}]')
                current_node = current_node.next
            else:
                nodes.append(f'[{current_node.name}]')
                current_node = current_node.next
        return "".join(nodes)


    def add_node(self, name, size=0):
        if self.tail is None:
            new_node = Node(name, size)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = Node(name, size)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None

    

tree = SystemTree()
tree.add_node("/")
tree.add_node("A")
tree.add_node("f", 29116)
tree.add_node("g", 2557)
tree.add_node("h.lst", 62596)
tree.add_node("E")
tree.add_node("b.txt", 14848514)
tree.add_node("c.dat", 8504156)
tree.add_node("D")
tree.add_node("j", 4060174)
tree.add_node("d.log", 8033020)
tree.add_node("d.txt", 5626152)
tree.add_node("k", 7214296)

print(tree)