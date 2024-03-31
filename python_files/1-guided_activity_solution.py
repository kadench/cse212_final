# This simple Queue class allows us to use the
# methods and class names discussed on this page
class Queue:

    # When Queue() is called, a new instance of Queue()
    # is created and a list named 'items' is used as its base.
    def __init__(self):
        self.items = []
    
    # When enqueue() is called, the requested enqueue item will
    # be appended to the queue
    def enqueue(self, item):
        self.items.append(item)

    # When dequeue() is called, it removes the item in front of
    # the queue only if the list has data inside of it. This makes
    # use of the .empty() method
    def dequeue(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            # (uncomment to use if needed)
            # print('The queue is empty') # Tell dev queue is
            # empty, then return None
            return None

    # When empty() is called, it returns True if the queue is
    # empty and False when the queue is not 
    def empty(self):
        return len(self.items) == 0

    # size() returns the size of the queue as a number
    def size(self):
        return len(self.items)

    # Defining __iter__ here allows a Queue() the ability
    # to become iterable. This is because the yield keyword
    # creates a generator which returns each item in the queue
    # individually.  
    def __iter__(self):
        for item in self.items:
            yield item

# Make a new instance of the Queue class first
queue = Queue()

# Next add five people...
queue.enqueue('person1')
queue.enqueue('person2')
queue.enqueue('person3')
queue.enqueue('person4')
queue.enqueue('person5')

# ...then remove two
queue.dequeue()
queue.dequeue()

# Print each person in the queue
for x in queue:
   print(x)
