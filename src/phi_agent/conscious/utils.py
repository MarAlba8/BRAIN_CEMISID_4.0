from copy import copy


class MaxItemsError(Exception):
    pass


class Node:
    def __init__(self, key: str = ""):
        self.key = key
        self.next = None


class DescriptorQueue:
    MAX_SIZE = 4

    def __init__(self):
        self.head = None #Node()
        self.current = None #Node()
        self.tail = None #Node()
        self.size = 0

    # def get_current(self):
    #     return self.current

    def dequeue(self):
        self.head = self.head.next
        self.size -= 1
        return self.head

    def enqueue(self, key: str):
        if self.size >= self.MAX_SIZE:
            raise MaxItemsError("Maximum number of items reached")
        new_node = Node(key=key)
        #new_node.next = self.head
        if self.size == 0:
            self.head = new_node
            self.current = self.head

        # tail_next = self.tail.next
        # if not tail_next:
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1
        return self.tail

    def has_key(self, key: str):
        current = copy(self.head)

        while current:
            if current.key == key:
                return True
            current = current.next

            #if not next:
        return False

    def get_keys(self):
        keys = []
        current = copy(self.head)
        while current:
            keys.append(current.key)
            current = current.next
        return keys
