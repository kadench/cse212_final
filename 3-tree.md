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
<p align="center">
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
| [`BST()`](3-tree.md#size-example)  | Creates a new BST                                      |   **Depend on Method**  |
| [`.size()`](3-tree.md#size-example)                   | Returns the size of the BST as an int                    |   **O(1)**  |
| [`.empty()`](2-set.md#size-example)                   | Checks if BST is empty: True or False                  |   **O(1)**  |
| [`.insert(node)`](2-set.md#additem-example)  | Inserts an item into the BST                           |   **O(*log* n)**  |
| [`.remove(node)`](2-set.md#removeitem-example)  | Removes an item from the BST                    |   **O(*log* n)**  |
| [`.contains(value)`](2-set.md#unionset-example)       | Checks if the BST contains a certain number  |   **O(*log* n)**  |
| [`.height(node)`](2-set.md#intersectionset-example)    |  Returns the number of levels a number is from the root  |   **O(n)**  |
| [`.traverse_forward()`](2-set.md#memberitem-example)  | Prints all numbers in a BST starting from the root to the end |   **O(n)**  |
| [`.traverse_backward()`](2-set.md#memberitem-example) | Prints all numbers in a BST starting from the end to the root |   **O(n)**  |

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
As you probably know, with code, you need to tell the computer exactly what you want it to do. With the `.insert()` method, it's no different. The reason I bring this up is to talk about a new term you may not be familiar with: `recursion`. If you're familiar with what this is, or you just want to get the example, click [here]().
### *`.insert(node)` Example*
```python
1 # Make a BST
2 tree = BST()
3
4 # Inserts 5 in the BST
5 tree.insert(5)
```
## Contact
Comments or questions are welcome! Please feel free to contact me through my [school email](mailto:han22047@byui.edu).

This is my final project for CSE 212 or Programming w/ Data Structures. This is a course taught at BYU-I.

© 2024 Kaden Hansen. All Rights Reserved.