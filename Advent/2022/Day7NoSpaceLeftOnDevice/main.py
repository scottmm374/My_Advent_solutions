class Node:
    def __init__( self, name, size=0):
        self.name = name
        self.size = size
        self.children = []

def addChild(name, size=0):
    new_node = Node(name, size)
    return new_node


def traverse(root):
    if(root == None):
        return;

    que = []
    que.append(root)

    
    while len(que) != 0:
        x = len(que)

        # traverse if children
        while x > 0:

            parent = que[0]
            que.pop(0)
            print(f'{parent.name} is {parent.size} mb', end=' ')

            for i in range(len(parent.children)):
                que.append(parent.children[i])
            x -= 1
        print()

if __name__ == "__main__":
    root = Node("/")
    root.children.append(addChild("A"))
    root.children.append(addChild("b.txt", 14848514))
    root.children.append(addChild("c.dat", 8504156))
    root.children.append(addChild("D"))
    root.children[0].children.append(addChild("E"))
    root.children[0].children[0].children.append(addChild("i", 584))
    root.children[0].children.append(addChild("f", 29116))
    root.children[0].children.append(addChild("g", 2557))
    root.children[0].children.append(addChild("h.lst", 62596))

    root.children[3].children.append(addChild("j", 4060174))
    root.children[3].children.append(addChild("d.log", 8033020))
    root.children[3].children.append(addChild("d.exe", 5626152))
    root.children[3].children.append(addChild("k", 7214296))

    print(traverse(root))