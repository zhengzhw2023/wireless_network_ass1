class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    # Usage example


q = Queue()
print("Is the queue empty?", q.is_empty())  # Output: True

q.enqueue("Apple")
q.enqueue("Banana")
q.enqueue("Cherry")

print("Queue size:", q.size())  # Output: 3

print("Dequeued item:", q.dequeue())  # Output: Apple
print("Dequeued item:", q.dequeue())  # Output: Banana

print("Queue size:", q.size())  # Output: 1
print("Is the queue empty?", q.is_empty())  # Output: False

print("Remaining item:", q.dequeue())  # Output: Cherry
print("Is the queue empty?", q.is_empty())  # Output: True