"""
You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.

we have two pointers. one is a iteration pointer and the other will be behind it by requested number of elements. so for example lets say we need to get value of 3rd element from tail. we start incrementing second pointer after 3rd element alongside with iteration pointer. When iteration pointer gets to the end(tail) second pointer is going to be pointing to 3rd element from it. which is our answer. Think about two cars: C(current) and R(result). They have the same speed and C is in fromt of R. The distance between them is the value of positionFromTail. So when C arrive at the ending point, where is R? Note that their distance is "positionFromTail", the position of R is the position from tail.

You have to complete the int getNode(SinglyLinkedListNode* head, int positionFromTail) method which takes two arguments - the head of the linked list and the position of the node from the tail. positionFromTail will be at least 0 and less than the number of nodes in the list. You should NOT read any input from stdin/console.
"""


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


def getNode(head, positionFromTail):
    trailingNode = head
    len = 0
    while (head):
        if (len > positionFromTail):
            trailingNode = trailingNode.next
        len += 1
        head = head.next
    return trailingNode.data


if __name__ == '__main__':
    array = [23, 34, 56, 45, 78, 87, 2, 20]
    position_from_back = 4
    llist = SinglyLinkedList()
    for i in range(len(array)):
        llist_item = array[i]
        llist.insert_node(llist_item)
    llist.printLL()
    result = getNode(llist.head, position_from_back)
    print(result)
