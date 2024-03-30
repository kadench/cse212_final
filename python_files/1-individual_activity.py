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

import random # adds the ability to add people at random into the queue

movie_queue = Queue()  # Create a new movie-goer queue

# Define line constants (cannot change)
MAX_MOVIE_QUEUE_SIZE = 10 # The max size of the queue is ten

# If the movie queue has room for more people
while movie_queue.size() < MAX_MOVIE_QUEUE_SIZE:
    person = random.choice(['person_yes_ticket', 'person_no_ticket']) # Simulate the different people who come to the theater.

    # Don't allow them to enter the movie line unless they have a ticket
    if person == 'person_yes_ticket':
        movie_queue.enqueue(person)
    else:
        # Tell the person without a ticket that they need one to see the movie.
        print("We're sorry, but you need to buy a valid ticket before you can enter the theater.")

# Show the people in the queue, ensuring that they all have tickets and that there's no more than 10 people in the queue.
print(f"There are {movie_queue.size()} people waiting to see the movie.")

for i, person in enumerate(movie_queue):
    print(f"{i + 1}. {person}")
