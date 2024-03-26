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

### Common Methods Used in a Queue:
| Function        | Definition                                | Performance |
|:---------------:|:-----------------------------------------:|:-----------:|
| `.enqueue(item)` | Add an item to the back of the queue.    | **O(1)**        |
| `.dequeue()`     | Remove the first item from the queue.    | **O(1)**        |
| `.empty()`       | Checks if the queue is empty.            | **O(1)**        |
| `.front()`       | Returns a copy of the first item in the queue. | **O(1)**      |
| `.rear()`        | Returns a copy of the last item in the queue. | **O(1)**      |
| `.size()`        | Returns the size of the list as a number. | **O(1)**       |




## Queue Operations

### Accessing Data in the Queue
Even though a queue has similar structure to a list, some things are different. When we want to retrieve data from a list in python, we can just set a certain index to a variable. Doing so allows us to use it later:

```python
foods = ['egg', 'salad', 'sandwich'] # make a list
eaten_food = my_list[2] # set list item to the lunch variable
print(f"I had {eaten_food} for lunch") # print the variable in a sentence
```


## Modifying Data in the Queue

### Adding an Item to the Queue

#### Enqueue

### Deleting an Item from the Queue

#### Dequeue

![enqueue_and_dequeue_small](https://github.com/kadench/cse212_final/assets/144969637/b66b37b2-1c12-42da-8c6c-b378feb9db7f)

# When to Use A Queue

# When ***NOT*** to Use A Queue

# Practice Using Queue

## Example Problem Using a Queue (w/ Answer)

## Example Problem Using a Queue (Individually)

## Contact
Comments or questions are welcome! Please feel free to contact me through my [school email](mailto:han22047@byui.edu).

This is my final project for CSE 212 or Programming w/ Data Structures. This is a course taught at BYU-I.

© 2024 Kaden Hansen. All Rights Reserved.