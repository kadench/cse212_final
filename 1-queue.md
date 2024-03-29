### **CSE 212 Python Fundamentals Tutorial | An Introduction to Queues**

#### By: Kaden Hansen

|                Other Content              |
|:-----------------------------------------:|
| [Welcome](0-welcome.md)                   |
| [An Introduction to Queues (you're here)](1-queue.md)   |
| [An Introduction to Sets](2-set.md)       |
| [An Introduction to Trees](3-tree.md)     |

# **Queues**

What is a **queue**? In Python, a **queue** is used to execute multiple items, one at a time, in the order they arrived. This methodology is referred to as `FIFO`, or `First in, First Out`. This can quickly be visualized through a line of emojis. Each of them are patiently waiting their turn for a hot dog:

### **Queue Example:**

```python
   # exit                                               # enter
c|:] dequeue <-- [':)', 'o/', ':]', '(:', '[:', '\o'] <-- enqueue
```
`:)` is first in line, which means he gets the first hot dog. Then, `:)` leaves and everyone else in line moves up one. It's exactly like how a line works in real life.

### Common Classes/Method Used in a Queue:
(Click the names of each item to see an example use case.)

| Class/Method Name        | Definition                                | Performance |
|:---------------:|:-----------------------------------------:|:-----------:|
| `Queue()`        | Makes a new queue                        | **O(1)**    |
| `.enqueue(item)` | Add an item to the back of the queue.    | **O(1)**    |
| `.dequeue()`     | Remove the first item from the queue.    | **O(1)**    |
| `.empty()`       | Checks if the queue is empty.            | **O(1)**    |
| `.front()`       | Returns a copy of the first item in the queue. | **O(1)**  |
| `.rear()`        | Returns a copy of the last item in the queue. | **O(1)**   |
| `.size()`        | Returns the size of the list as a number. | **O(1)**       |




## Queue Operations

### Accessing Data in the Queue
Even though a **queue** has similar structure to a list, it's not the same thing. To show difference between a list and a **queue**, there is an example of what we can do with the data in the different data types. When we want to retrieve data from a python list, we have many options, but with a queue, we need only the resulting queue or its results after a run through. See the two examples given below:

### Accessing Data in List Example:
```python
# Make a list of food items and set the eaten_food variable to the third index of
# the foods list

foods = ['egg', 'salad', 'sandwich']
eaten_food = my_list[2]

# Print the list item in a sentence
print(f"I had a {eaten_food} for lunch.")

# ======================================
# result: I had a sandwich for lunch.
```

With a **queue**, we usually don't retrieve the input, but rather the output. This is because for every item in the queue, there is usually an action to be performed. There's no need to get an object at a certain index. We can print the **queue** after it is processed to show the results:

### Accessing Data in Queue Example: 
```python
# Assuming the Queue class is defined with the methods described in the table above

queue = Queue()
queue.enqueue(138) # Adding an item to the queue
queue.enqueue(218)
queue.enqueue(363)
queue.enqueue(417)
queue.dequeue(218) # Removing an item from the queue

# Print all items in the queue with a for loop
for x in queue:
    print(x)

# ============================================
"""
result:
138
363
417
"""
```

# When to Use A Queue

# When ***NOT*** to Use A Queue

# Practice Using Queue

## Example Problem Using a Queue (w/ Answer)

## Example Problem Using a Queue (Individually)

## Contact
Comments or questions are welcome! Please feel free to contact me through my [school email](mailto:han22047@byui.edu).

This is my final project for CSE 212 or Programming w/ Data Structures. This is a course taught at BYU-I.

© 2024 Kaden Hansen. All Rights Reserved.