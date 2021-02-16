'''Write a double-ended LinkedList class
You should have a Link class
It should keep a reference to next and prev.
You should have a LinkedList class
It should have first and last methods to return the first/last links
in the list, or undefined if the list is empty.
It should have push and pop methods.
You should write a remove method that takes in a value and removes
the first link found with that value.
Given a linked list of integers and an integer value, delete every node
of the linkedlist containing that value. '''


class Link:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Link()
        self.tail = Link()
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        return self.head.next == self.tail

    def first(self):
        if self.is_empty():
            return None
        return self.head.next

    def last(self):
        if self.is_empty():
            return None
        return self.tail.prev

    def push(self, value):
        # don't have to return since mutating
        newLink = Link(value)
        last = self.last()
        last.next = newLink
        newLink.prev = last
        newLink.next = self.tail
        self.tail.prev = newLink

    def pop(self):
        last = self.last()
        if not last:
            return None
        before_last = last.prev
        before_last.next = self.tail
        self.tail.prev = before_last
        last.prev = None
        last.next = None
        return last

    def find(self, value):
        if self.is_empty():
            return None
        current_link = self.first()
        while current_link:
            if current_link.value == value:
                return current_link
            current_link = current_link.next
        return None

    def remove(self, value):
        if self.find(value):
            link = self.find(value)
            previous = link.prev
            nextLink = link.next
            previous.next = nextLink
            nextLink.prev = previous
            link.next = None
            link.prev = None
            return link
        return None

    def delete_every(self, value):
        while self.find(value):
            self.remove(value)
