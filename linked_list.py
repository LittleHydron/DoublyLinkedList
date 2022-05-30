class DoublyLinkedList:
    class Node:
        def __init__(self, content) -> None:
            self.content = content
            self.child = None
            self.parent = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push_back(self, content) -> None:
        if self.tail is None:
            self.tail = self.Node(content)
            self.head = self.tail
        else:
            self.tail.child = self.Node(content)
            self.tail.child.parent = self.tail
            self.tail = self.tail.child

    def sort_by_selection(self) -> None:
        tmp = self.head
        while tmp is not None:
            tmp1 = tmp.child
            while tmp1 is not None:
                if tmp1.content < tmp.content:
                    tmp1.content, tmp.content = tmp.content, tmp1.content
                tmp1 = tmp1.child
            tmp = tmp.child

    def print_list(self) -> None:
        node = self.head
        while node is not None:
            print(node.content)
            node = node.child

    def print_by_mark(self, mark: str) -> None:
        node = self.head
        while node is not None:
            if node.content.mark == mark:
                print(node.content)
            node = node.child
