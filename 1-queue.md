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
# Exit                                                   # Enter
c|:] dequeue <-- [':)', 'o/', ':]', '(:', '[:', '\o'] <-- enqueue
```
`:)` is first in line, which means he gets the first hot dog. Then, `:)` leaves and everyone else in line moves up one. It's exactly like how a line works in real life.

### Common Classes/Method Used in a Queue:
(Click the names of each item to see an example use case.)

| Class/Method Name                                       | Definition                                | Performance |
|:-------------------------------------------------------:|:-----------------------------------------:|:-----------:|
| [`Queue()`](1-queue.md#accessing-data-in-queue-example) | Makes a new queue | **O(1)**                            |
| [`.enqueue(item)`](1-queue.md#accessing-data-in-queue-example) | Add an item to the back of the queue. | **O(1)** |
| [`.dequeue()`](1-queue.md#accessing-data-in-queue-example) | Remove the first item from the queue.  | **O(1)**    |
| [`.empty()`](1-queue.md#queue-empty-example) | Checks if the queue is empty. |                  **O(1)**          |
| [`.size()`](1-queue.md#queue-size-example) | Returns the size of the list as a number. | **O(1)**                 |




## Queue Operations

### **Accessing Data in the Queue**
Even though a **queue** has similar structure to a list, it's not the same thing. To show difference between a list and a **queue**, there is an example of what we can do with the data in the different data types. When we want to retrieve data from a python list, we have many options, but with a queue, we need only the resulting queue or its results after a run through. See the two examples given below:

### *Accessing Data in List Example 1:*
```python
1 # Define a list of foods
2 foods = ['egg', 'salad', 'sandwich']
3
4 # Set eaten_food to the third index of the list.
5 eaten_food = foods[2]
6
7 # Print the list item in a sentence
8 print(f"I had a {eaten_food} for lunch.")
9
10 # ======================================
11 # Example 1 result: I had a sandwich for lunch.
```
### *Accessing Data in List Example 2:*
```python
1 # Define a list of foods
2 foods = ['egg', 'salad', 'sandwich']
3
4 # for each food in foods, print it in a sentence
5 for eaten_food in foods:
6     print(f"I had a(n) {eaten_food} for lunch.")
7 
8 # ======================================
9 # Example 2 results:
10 # I had a(n) egg for lunch.
11 # I had a(n) salad for lunch.
12 # I had a(n) sandwich for lunch.
```
---
With a **queue**, we usually don't retrieve the input, but rather the output. This is because for every item in the queue, there is usually an action to be performed. If there's not a certain action to be done with each item, adding them to the **queue** is, in itself, an action. There's no need to get an object at a certain index. We can print the **queue** after it is processed to show the results:

### *Accessing Data in Queue Example:* 
```python
1 queue = Queue() # Creating an empty queue
2  
3 queue.enqueue(138) # Adding 138 to the queue
4 queue.enqueue(218) # Adding 218 to the queue
5 queue.enqueue(363) # Adding 363 to the queue
6 queue.enqueue(417) # Adding 417 to the queue
7  
8 queue.dequeue() # Removing the front item from the queue
9 
10 # Print all items in the queue with a for loop
11 for x in queue:
12     print(x)
13 
14 # ============================================
15 # result:
16 # 218
17 # 363
18 # 417
```
In this example, a new instance of `Queue()` is created. This allows us to use a `for` loop to return all the new items in it later on. This is used to visualize what's inside the **queue**. We see that 218, 363, and 417 are the numbers printed by the `for` loop. This is because `enqueue()` was used to add the numbers to the queue. While 138 was added to the queue using the same method, it was removed when `dequeue()` was called.

If you're unsure why 138 (the first number added to the **queue**) was removed instead of 417 (the last number added to the **queue**), look back at the queue [example](1-queue.md#queue-example). The **dequeue** is found at the front of the line. Therefore, 138 was removed from the **queue** when `dequeue()` was called. 

### **Queue Length**
Getting and using the length of a queue can be a very useful tool when setting conditions, executing certain functions, or running a program. A good example that use something similar to the **queue's** `empty()` and `size()` methods is a printer. A printer receives documents in the order that they arrived, it prints them, and shuts off. The only reason the printer knows how to shut off is because of the check to make sure all documents are done printing. Below, you can see a mock printer that uses the `empty()` method to shut off when done. 
### *Queue `empty()` Example:*
```python
1 printing_queue = Queue()  # Define a new printing queue
2
3 # Add new documents to the queue as tuples: (document name, total page count)
4 printing_queue.enqueue(('example.docx', 3))
5 printing_queue.enqueue(('example1.docx', 2))
6
7 # While the queue is not empty
8 while not printing_queue.empty():
9 
10     # set the contents of the dequeued tuple to the respective variable names
11     document, total_pages = printing_queue.dequeue()
12
13     # For each page in the current document
14     for current_page in range(1, total_pages + 1):
15        
16          # Show which page of the current document your printing
17          print(f"Printing page {current_page} of {document}.")
18        
19          # ... print it
20    
21     # Show that the certain document has finished printing
22     print(f"Finished printing {document}.")
23
24 # If all the documents are done printing, notify and shut off
25 print("All documents have been printed.")
```
As you can see, the program makes sure it has documents in the **queue** before it tries to print anything. It'd be very annoying if this didn't happen. It's simple, but very important.

 Moving on, a good example with the use of `.size()` is its use in a **priority queue**. A **priority queue** is almost the same as a normal **queue**. However, some items in this **queue** have a reason to be placed in front of other items that don't have a certain importance. An example of this is a paid subscription that grants up to 45 paying members a shorter wait time in a line compared to 15 non-paying players that can join too with a standard wait time. The size checking portion of this scenario can be done with the example below (The advancement in line based on status isn't shown here for the sake of simplicity):
 ### ***Queue `.size()` Example:***
```python
1 import random
2 
3 queue = Queue()  # Create a new player queue
4 
5 MAX_QUEUE_SIZE = 60 # The player queue cannot exceed 60 players per server
6 MAX_NON_PAYING_MEMBERS = 15 # 25% of the server's queue can be free members
7  
8 # The number of each member type in the queue
9 paying_members_count = 0
10 non_paying_members_count = 0
11
12 # As long as the queue size is less than 60
13 while queue.size() < MAX_QUEUE_SIZE:
14 
15     # If there is still room for free members 
16     if non_paying_members_count < MAX_NON_PAYING_MEMBERS:
17
18          # pick player at random (for example purposes)
19          member_choice = random.choice(['Paying', 'Non-Paying']) 
20     else:
21          member_choice = 'Paying' # The choice is automatically Paying
22     
23     # Find out the member choice and tick that certain member count up by 1
24     if member_choice == 'Paying':
25          paying_members_count += 1
26     else:
27          non_paying_members_count += 1
28     
29     # Add the new member to the queue
30     queue.enqueue(member_choice + ' Member')
31 
32 # Show the number of free and paying players in the queue.
33 print(f"Total members in queue: {queue.size()}")
34 print(f"Paying members: {paying_members_count}, Non-Paying members: {non_paying_members_count}")
```
`.size()` is being used as a check here to ensure no more than 25% of the 60 max players are free users. This can be used as an incentive to have users pay for a better chance to play.
# Practice Using Queue

## Example Problem Using a Queue (w/ Answer)

## Example Problem Using a Queue (Individually)

## Contact
Comments or questions are welcome! Please feel free to contact me through my [school email](mailto:han22047@byui.edu).

This is my final project for CSE 212 or Programming w/ Data Structures. This is a course taught at BYU-I.

© 2024 Kaden Hansen. All Rights Reserved.