### **CSE 212 Python Fundamentals Tutorial | An Introduction to Trees**

#### By: Kaden Hansen

|               Other Content               |
|:-----------------------------------------:|
| [Welcome](0-welcome.md)                   |
| [An Introduction to Queues](1-queue.md)   |
| [An Introduction to Sets](2-set.md)       |
| [An Introduction to Trees (you're here)](3-tree.md) |



## **Introduction**
### What is a Tree?
In Python, a **tree** is a data structure that is used to store related and measurable data. For example, numbers have a measurable value. When storing numbers by their value in a **tree**, we find the **root** value, or the beginning of the tree. In the case of numbers, it's the number that will allow the most connections down in the line. The middle ground if you will. An easy way to visualize or see a tree in action is to look at your family tree. Each person is considered a **node** or an item that relates to the previous item in the tree.

### Family Tree Example:

<div style="padding-top: 6px">
<p align="center">
  <img style="max-height: 360px" src="https://github.com/kadench/cse212_final/assets/144969637/f74b6b68-c1be-44a3-8643-03de81240b04"/>
<p align="center"><strong>Family Tree Example</strong> by: Kaden Hansen</p>
<p align="center"></p>
</p>
</div>

A family tree, like the one above, is a bit different from a tree data structure, but it's still a good representation nonetheless. There is a pair of root nodes that branch downward. These root nodes (labeled with P) are the parents of the next generation. The **leaves** of a tree are at the end of the tree and cannot become a **subtree** as they are not connected to further things down the line. A subtree can only exist if there are parents and children after the last set of parents. A colored representation is shown 

### Family Tree Legend:

<div style="padding-top: 6px">
<p align="center">
  <img style="max-height: 440px" src="https://github.com/kadench/cse212_final/assets/144969637/f399b149-9ef0-486f-a886-eb2f36b807e6"/>
<p align="center"></p>
</p>
<p align="center"><strong>Family Tree Legend</strong> by: Kaden Hansen (Stylistic fake cursor in image)</p>
</div>

The trees we're talking about will be and act a little differently. A **Binary Tree** has one root and each node that follows connects to two nodes at maximum. A `BST()` or **Binary Search Tree** is a formulated way that data can be placed into a tree. This is done by comparing the values existing in the tree already with the data presently being added to the tree. When we do this with numbers, we compare the new number to the root node in the tree.

If the new number is greater than the root number, it moves down one level to the **right**. If the number is less than the root, it moves down one level to the **left**. It then compares itself to all the numbers in the tree, repeating this action until an empty space is found.

### What is the Purpose of a Tree?
The main purpose of any type of tree (data structure) is to organize data in a simple and searchable format. For example, when setting up a `BST()` up in this way (if balanced) has the Big O Notation of O(log n). This means that as we want to find if a number exists in the tree or add a new number, it cuts the search time in half every level gone down.

If your stuck and need more of a guide, look at `9` (the root) in the image below. You're looking for `5`. If it is lower than the number you're on, move down one level to the left. If the number you're looking for is greater than the number you're on, move down one level to the right. When you've done it right, you should be on `5`.

<div style="padding-top: 6px">
<p align="center" id="bst-example">
  <img src="https://github.com/kadench/cse212_final/assets/144969637/3b91cf5f-e123-4860-a876-7d87dd5b625a"/>
<p align="center"></p>
</p>
<p align="center"><strong>Finding 5 in the Given Tree</strong></p>
</div>

> **Note:** If you don't know what O(n) means, there's an [introduction](0-welcome.md#introduction--big-o-notation-or-on) on the welcome page.

---

### Common Tree Methods:
(Click the names of each item to see an example use case.)

| Class/Method Name                                        | Definition                                             | Performance |
|:--------------------------------------------------------:|:------------------------------------------------------:|:-----------:|
| [`BST()`](3-tree.md#bst-example)  | Creates a new BST                                      |   **Depend on Method**  |
| [`.size()`](3-tree.md#size-examplee)                   | Returns the size of the BST as an int                    |   **O(1)**  |
| [`.empty()`](3-tree.md#empty-example)                   | Checks if BST is empty: True or False                  |   **O(1)**  |
| [`.insert(node)`](3-tree.md#insertnode-example)  | Inserts an item into the BST                           |   **O(*log* n)**  |
| [`.remove(node)`](3-tree.md#remove-example)  | Removes an item from the BST                    |   **O(*log* n)**  |
| [`.contains(value)`](3-tree.md#remove-example)       | Checks if the BST contains a certain number  |   **O(*log* n)**  |
| [`.height(node)`](3-tree.md#remove-example)    |  Returns the number of levels a number is from the root  |   **O(n)**  |
| [`.traverse_forward()`](3-tree.md#remove-example)  | Prints all numbers in a BST starting from the root to the end |   **O(n)**  |
| [`.traverse_backward()`](3-tree.md#remove-example) | Prints all numbers in a BST starting from the end to the root |   **O(n)**  |

## Tree Operations
Down below is an example of each method found in the method table [above](3-tree.md#common-tree-methods):
### *`.size()` Example:*
```python
1 # Make a new BST
2 tree = BST()
3
4 # .. do what you need with the BST
5
6 # Use a formatted string to print tree's size
6 print(f"The size of the current BST: {tree.size()}")
```
> The size of the current BST: 0

Nothing was added to the `BST()` in this example, so the size of `tree` is `0`.

---

### *`.empty()` Example:*
```python
1 # Make a BST
2 tree = BST()
3
4 # .. do what you need with the BST
5
6 # Use a formatted string to print .empty's return.
7 print(f"There are no items in tree: {tree.empty()}")
```
> There are no items in tree: True

`tree` has no nodes inside of it, so the return is **True**. This method makes use of `.size()` which validates it against **0**. If the size of `tree` is **0**, `.empty()` will return True else, False.

---
### `.insert(node)`
As you probably know, with code, you need to tell the computer exactly what you want it to do. With the `.insert()` method, it's no different. The reason I bring this up is to talk about a new term you may not be familiar with: `recursion`. If you're familiar with what this is, or you just want to get the example (I'd encourage you to read it in this case), click [here](3-tree.md#insertnode-example).

# Recursion
**Recursion** is a useful tool that we can use in a lot of ways. I can even make a whole other lesson on this, but in short, we use recursion to repeatedly call on the same function inside itself to reduce code and increase space efficiencies. However, this recursion cannot occur infinitely and will end in a `RecursionError` if called too many times. Below is a quick example of recursion.
### *Recursion Example*:
```python
1 def recursion_example():
2    print("This is an example of recursion.")
3    recursion_example() # Call the function repeatedly until the error occurs
4 recursion_example() # Initiate the recursive action
=================================================
Recursion Example Result:
This is an example of recursion.
This is an example of recursion.
This is an example of recursion. # repeated 997 more times
RecursionError: maximum recursion depth exceeded while calling a Python object
```

To stop the `RecursionError` from happening, we need a **base case**, or a case, when met, that will stop the repeated call (before the recursion limit). This is a smaller case that will be met in order to keep the program running. A base case with the above example can look like this:

### *Recursion Example (w/ Base Case)*:
```python
1 def recursion_example(MAX_RECURSE, recurse_index:int = 0):
2     # Define the base case
3     if recurse_index == MAX_RECURSE:
4         return # Stop the recursion because the requested amount of prints have been reached
5     
6     # Define the recursive case
7     else:
8         print("This is an example of recursion.")
9         recurse_index += 1 # Increase the recurse index to keep score of prints
10        # Call the function repeatedly until the max recurse index is met.
11        recursion_example(MAX_RECURSE, recurse_index) 
12
13 recursion_example(4) # Initiate the recursive action with a max recurse of 4
=================================================
Recursion Example (w/ Base Case) Result:
This is an example of recursion.
This is an example of recursion.
This is an example of recursion.
This is an example of recursion. # Stops at 4 recursions because of the base case
```
As you can see, a **base case** is implemented to stop the `recursion_example()` function from running too many times. In a simple, standard recursive function, we find a **base case** and a **recursive case**. The recursive part of the function will continue to run until the base case is met.
> This was just a simple rundown of `recursion`. If you need more info, read the Python recursive walkthrough on [w3schools.com](https://www.w3schools.com/python/gloss_python_function_recursion.asp).


### *`.insert(node)` Example*
```python
1 # Make a BST
2 tree = BST()
3
4 # Inserts 5 in the BST
5 tree.insert(5)
```
Now, you may be wondering why I rushed through the explanation of `recursion`, but I promise it is necessary. A tree uses recursion everywhere when fulfilling its tasks. I thought it fitting to put it before `.insert(node)` because when you **insert** a node into a tree, the function uses recursion to snugly fit the new node where it needs to go. (This will not be shown until the end.)

---

### *`.remove()`:*
While `.insert()` and `.remove()` both use recursion to find a position in the tree, `.insert()` finds an empty spot in the tree with the method described [above](3-tree.md#what-is-the-purpose-of-a-tree) and places the new node there while `.remove()` has some special cases to reorganize the tree after the specific node has been deleted. Some of these are:

| Things that need to happen after a node is removed | Result |
|:--------------------------------------------------:|:------:|
| **The node is a leaf** | You can just remove this without any reorganization |
| **The node has one child** | The child takes the place of the parent. |
| **The node has two children** | See below |

When a parent node has two children, it gets a little more complicated. We need to one, make sure the tree stays structured and organized the with the lesser values gone on the left and the greater values to the right of a number at a given point.

### *`.remove()` Example:*
```python
1 # Make a BST
2 tree = BST()
3
4 # Insert 15 into the BST
5 tree.insert(15)
6
7 # Remove 15 from the BST
8 tree.remove(15)
```

> I didn't have enough time to finish the assignment before the due date. This is because it took too long to put the other lessons together, and I am on a trip that has made it hard for me to finish this assignment. However, I do feel confident in the other two pages to have the whole thing be graded at this point.


## Contact
Comments or questions are welcome! Please feel free to contact me through my [school email](mailto:han22047@byui.edu).

This is my final project for CSE 212 or Programming w/ Data Structures. This is a course taught at BYU-I.

© 2024 Kaden Hansen. All Rights Reserved.