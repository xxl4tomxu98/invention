"""Given a reference to the head of a doubly-linked list and an integer,
create a new DoublyLinkedListNode object having data value  and insert
it into a sorted linked list while maintaining the sort.

Function Description: Complete the sortedInsert function in the editor
below. It must return a reference to the head of your modified
DoublyLinkedList.

sortedInsert has two parameters:
head: A reference to the head of a doubly-linked list of DoublyLinkedListNode
objects.

data: An integer denoting the value of the  field for the DoublyLinkedListNode
you must insert into the list.

Note: Recall that an empty list (i.e., where ) and a list with one element are
sorted lists."""


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)
    if not head:
        head = newNode
    else:
        n = head
        if head.data >= data:
            head = newNode
            head.next = n
            n.prev = head
        else:
            while(n.next and n.next.data < data):
                n = n.next
            n_next = n.next
            n.next = newNode
            n.next.next = n_next
    return head

# def sortedInsert(head, data):
#     newNode = DoublyLinkedListNode(data)
#     if (head == None):
#         return newNode
#     elif (data < head.data):
#         newNode.next = head
#         head.prev = newNode
#         return newNode
#     else:
#         newNode = sortedInsert(head.next, data)
#         head.next = newNode
#         newNode.prev = head
#         return head


def printNewDoubleLinkedList(node):
    while node:
        print(str(node.data))
        node = node.next


if __name__ == '__main__':
    array = [5]
    data = 1
    llist = DoublyLinkedList()
    for i in range(len(array)):
        llist_item = array[i]
        llist.insert_node(llist_item)
    newHead = sortedInsert(llist.head, data)
    printNewDoubleLinkedList(newHead)
