"""You’re given the pointer to the head node of a linked list, an integer
to add to the list and the position at which the integer must be inserted.
Create a new node with the given integer, insert this node at the desired
position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from
the head and so on. The head pointer given may be null meaning that the initial
list is empty.

As an example, if your list starts as  and you want to insert a node at
position  with , your new list should be

Function Description Complete the function insertNodeAtPosition in the editor
below. It must return a reference to the head node of your finished list.

insertNodeAtPosition has the following parameters:

head: a SinglyLinkedListNode pointer to the head of the list
data: an integer value to insert as data in your new node
position: an integer position to insert the new node, zero based indexing"""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    """ def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node """

    # The following is alternate insertion method
    def insert_node(self, data):
        newNode = SinglyLinkedListNode(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


def insertNodeAtPosition(head, data, position):
    n = head
    if position == 0:
        head = SinglyLinkedListNode(data)
        head.next = n
    else:
        for _ in range(position-1):
            n = n.next
        n_next = n.next
        n.next = SinglyLinkedListNode(data)
        n.next.next = n_next
    return head


def printNewLinkedList(node):
    while node:
        print(str(node.data))
        node = node.next


if __name__ == '__main__':
    array = [23, 34, 56, 45, 78, 87, 2, 20]
    position = 0
    data = 30
    llist = SinglyLinkedList()
    for i in range(len(array)):
        llist_item = array[i]
        llist.insert_node(llist_item)
    newHead = insertNodeAtPosition(llist.head, data, position)
    printNewLinkedList(newHead)
