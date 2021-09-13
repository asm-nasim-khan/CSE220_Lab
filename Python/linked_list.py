class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.size=0

    # Inserting Values at the Beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size+=1

    # Inserting Values at the ending
    def insert_at_endning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.size += 1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        self.size += 1

    # Inserting Values From List at the end
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_endning(data)

    # Get the length of the linked list
    """def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
"""
    # Removing an element on given index
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid Index")
        self.size -= 1
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.size:
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                self.size += 1
                break
            itr = itr.next

    def remove_by_value(self, data):
        if data == self.head.data:
            self.head = self.head.next
            self.size -= 1
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                self.size -= 1
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print("HEAD=" + llstr + f"None\nSize of the following linked list is {self.size}\n")


ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.print()
ll.remove_by_value("mango")
ll.print()
ll.remove_by_value("apple")
ll.print()
ll.remove_by_value("grapes")
ll.print()
