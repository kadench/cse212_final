### **CSE 212 Python Fundamentals Tutorial | An Introduction to Sets**

#### By: [name here]

|                Other Content              |
|:-----------------------------------------:|
| [Welcome](0-welcome.md)                   |
| [An Introduction to Queues](1-queue.md)   |
| [An Introduction to Sets (you're here)](2-set.md)       |
| [An Introduction to Trees](3-tree.md)     |

# **Sets**

What is a `set()`? In Python, a set is an unordered collection of data. The only catch is that each datum inside the set has to be unique. There cannot be a duplicate in one set. Python uses hashing to add, remove, or entirely change the contents of a set which, in return, is extremely fast.

Hashing something like a `list()` is impossible because the data inside a list can change. Only immutable items can be added to a set. Immutable meaning data or collections of data that cannot change once created. This is the same reason why you cannot set a list as a key in a `dictionary()`. In the examples shown below, each set has the whole numbers 1-10:

### **Set Example (Using the keyword):**

```python
example_set = set(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

### **Set Example (Without the Keyword):**

```python
example_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
> Notice how neither of the example sets have a duplicate number. 

### Common Set Methods:
(Click the names of each item to see an example use case.)

| Class/Method Name                                        | Definition                                             | Performance |
|:--------------------------------------------------------:|:------------------------------------------------------:|:-----------:|
| [`set()`](2-set.md#additem-example)                      | Creates a new set                                      |   **O(1)**  |
| [`.add(item)`](2-set.md#additem-example)                 | Adds a unique item to a set                            |   **O(1)**  |
| [`.remove(item)`](2-set.md#removeitem-example)           | Removes a specified item from a set                    |   **O(1)**  |
| [`.union(set)`](2-set.md#unionset-example)               | Creates a set with the different items from both sets. |   **O(1)**  |
| [`.intersection(set)`](2-set.md#intersectionset-example) | Creates a set with the common items from both sets.    |   **O(1)**  |
| [`.size()`](2-set.md#size-example)                       | Returns the size of a set as an int                    |   **O(1)**  |
| [`.member(item)`](2-set.md#memberitem-example)           | Checks if a specified item is in a set                 |   **O(1)**  |



## Set Operations
Lets see an example of each `set()` method in action. Starting with `.add(item)`
### *`.add(item)` Example:* 
```python
1 # Define the current set
2 number_set = {1, 2, 3, 4}
3
4 # Add 5 to the set
5 number_set.remove(5)
6
7 # Print the resulting set
8 print(number_set)
```
> Output:
>
> {1, 2, 3, 4, 5}

5 was added to the `set()`.

---

### *`.remove(item)` Example:* 
```python
1 # Define the current set
2 number_set = {1, 2, 3, 4, 5}
3
4 # Remove 5 from the set
5 number_set.remove(5)
6
7 # Print the resulting set
8 print(number_set)
```
> Output:
>
> {1, 2, 3, 4}

5 was removed from the `set()`.

---

`.union(set)` will combine two different sets, and skip over any duplicates found.

### *`.union(set)` Example:* 
```python
1 # Define the current number set
2 number_set = {1, 2, 3, 4, 5}
3 
4 # Define a new letter set
5 letter_set = {"a", "b", "c", "d",}
6
7 # Combine both sets as a new set
8 united_set = number_set.union(letter_set)
9
10 # Print the resulting set
11 print(united_set)
```
> Output:
>
> {1, 2, 3, 4, 5, 'a', 'b', 'c', 'd'}

`letter_set` and `number_set` have been combined into the `united_set`. (Results will vary as a set is an unordered collection of data.)

---

`.intersection(set)` will put the common items of two specified sets into a new set, still skipping over any duplicates (if that item is in the intersected set already).

### *`.intersection(set)` Example:* 
```python
1 # Define a set of numbers, incrementing by 1, that starts at 0
2 counting_by_one = {0, 1, 2, 3, 4, 5}
3 
4 # Define a set of numbers, incrementing by 2, that starts at 0
5 counting_by_two = {0, 2, 4, 6, 8}
6
7 # Combine both sets as a new set
8 set_overlap = counting_by_one.intersection(counting_by_two)
9
10 # Print the resulting set
11 print(set_overlap)
```
> Output:
>
> {0, 2, 4}

`counting_by_one` and `counting_by_two`'s overlapping numbers have been added to the new `set_overlap` set. 

## Useful Methods That Don't Come by Default

`.size()`, if implemented, will return the size of a set at a given point.

### *`.size()` Example:* 
```python
1 # Define the current set
2 number_set = {1, 2, 3, 4}
3
4 # print the size of the set
5 print(f"The length of the set is: {number_set.size()}")
```
> Output:
>
> The length of the set is: 5

The correct length was returned for use in the print statement.

---

`.member()`, if implemented, will return **False** if a specified item doesn't exist, or **True** if the item does exist in the `set()`

### *`.member(item)` Example:* 
```python
1 # Define the current set
2 number_set = {1, 2, 3, 4, 5}
3
4 # Check if 5 is in the set and notify the user
5 if number_set.member(5)
6     print("The number exists in the set.")
7 else:
8     print("The number does not exist in the set.")
```
> Output:
>
> The number exists in the set.
## Practice Using Set
Now that you've been introduced to **sets** and have a basic understanding, let's do some practice problems.

### `Set()` Class:
```python
# This simple Set class allows us to use the
# methods and class names discussed on this page
class Set:
    # Set class implementation
```
> Download [set_class.py](python_files\set_class.py)

## Practice Problems

### 1. [First Problem Title]
[Problem description]

### **Solution:**

```python
# Solution code
```
> Download [solution_file.py](python_files/solution_file.py)

### 2. [Second Problem Title (Individual Activity)]

**Objective:** [Objective description]

**Guidance:**

- [Guidance]

**Challenge Yourself:**

[Challenge description]

> **Download Solution:** [solution_2.py](python_files/2-individual_activity.py)
