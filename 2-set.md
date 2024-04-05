### **CSE 212 Python Fundamentals Tutorial | An Introduction to Sets**

#### By: Kaden Hansen

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
# You will need to provide the data inside the curly
# brackets when doing it this way or else Python will
# think it's a dictionary!

example_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
> Notice how neither of the example sets have a duplicate number? 

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
> 
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
> 
>
> {1, 2, 3, 4}

5 was removed from the `set()`.

---

`.union(set)` will combine two different sets, and skip over any duplicates found.

### *`.union(set)` Example (long syntax):* 
```python
1 # Define a set containing numbers
2 number_set = {1, 2, 3, 4, 5}
3 
4 # Define a new letter set
5 letter_set = {"a", "b", "c", "d"}
6
7 # Combine both sets as a new set (long syntax)
8 united_set = number_set.union(letter_set)
9
10 # Print the resulting set
11 print(united_set)
```
> 
>
> {1, 2, 3, 4, 5, 'a', 'b', 'c', 'd'}
### *`.union(set)` Example (short syntax):* 
```python
1 # Define a set containing numbers 
2 number_set = {1, 2, 3, 4, 5}
3 
4 # Define a new letter set
5 letter_set = {"a", "b", "c", "d"}
6
7 # Combine both sets as a new set (short syntax)
8 united_set = number_set | letter_set # (result_set = set1 | set2 ..)
9
10 # Print the resulting set
11 print(united_set)
```
> 
>
> {1, 2, 3, 4, 5, 'a', 'b', 'c', 'd'}

`letter_set` and `number_set` have been combined into the `united_set`. (Results will vary as a set is an unordered collection of data.)

---

`.intersection(set)` will put the common items of two (or more) specified sets into a new set, still skipping over any duplicates (if that item is in the intersected set already).

### *`.intersection(set)` Example (long syntax):* 
```python
1 # Define a set of numbers, incrementing by 1, that starts at 0
2 counting_by_ones = {0, 1, 2, 3, 4, 5}
3 
4 # Define a set of numbers, incrementing by 2, that starts at 0
5 counting_by_twos = {0, 2, 4, 6, 8}
6
7 # Combine both set's common items into a new set (long syntax)
8 set_overlap = counting_by_ones.intersection(counting_by_twos)
9
10 # Print the resulting set
11 print(set_overlap)
```
> 
>
> {0, 2, 4}
### *`.intersection(set)` Example (short syntax):* 
```python
1 # Define a set of numbers, incrementing by 1, that starts at 0
2 counting_by_ones = {0, 1, 2, 3, 4, 5}
3 
4 # Define a set of numbers, incrementing by 2, that starts at 0
5 counting_by_twos = {0, 2, 4, 6, 8}
6
7 # Combine both set's common items into a new set (short syntax)
8 set_overlap = counting_by_ones & counting_by_twos # (common_results = set1 & set2 ..)
9
10 # Print the resulting set
11 print(set_overlap)
```
> 
>
> {0, 2, 4}

`counting_by_ones` and `counting_by_twos`'s overlapping numbers have been added to the new `set_overlap` set. 

## Useful Methods That Don't Come by Default
> We will **not** be using the methods discussed below in the practice problems. These methods don't come as default in Python.

`.size()`, if implemented, will return the size of a set at a given point.

### *`.size()` Example:* 
```python
1 # Define the current set
2 number_set = {1, 2, 3, 4}
3
4 # print the size of the set
5 print(f"The length of the set is: {number_set.size()}")
```
> 
>
> The length of the set is: 4

The correct length, `4`, was returned for use in the print statement.

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
> 
>
> The number exists in the set.

The number in the `set()` is correctly identified, and the corresponding message is returned.
## Practice Problems Using Set
Now that you've been introduced to **sets** and have a basic understanding, let's do some practice problems.

### 1. Jim & Jet Have A Set Regret (Guided Activity)
Jim and Jet are struggling to find a solution to the set problem they have been asked to solve. They need to make one new set that combines `even_number_set` and `odd_number_set`. This is what they have so far. Can you spot what they've done wrong?:

```python
1 # Create the odd and even sets
2 even_number_set = {0, 2, 4, 6, 10}
3 odd_number_set = {1, 3, 5, 7, 9}
4 
5 # Create the combined set to use later
6 combined_set = {}
7 
8 # Combine the two sets into one
9 combined_set.union(even_number_set, odd_number_set)
10 
11 # Print the resulting set.
12 print(combined_set)
```
> 
> AttributeError: 'dict' object has no attribute 'union'
> 
If you've figured out a solution to the problem, well done! You can keep reading this solution or move onto the next. If you haven't spotted the solution, there's a sneaky [hint](2-set.md#set-example-without-the-keyword) at the beginning of this lesson that might help you.

With that out of the way, there's a few problems that we need to address:

| Problems |
|----------|
+ `combined_set` is defined as the wrong data type.
+ `.union()` is formatted incorrectly.

<br>

In Python, a `dictionary()` is defined with curly braces **{ }**. If we don't deliberately tell the program that we're trying to make a `set()`, (by adding items separated by commas in the braces), it will automatically assume we're making a dictionary. A dictionary doesn't have the same methods a set does, making it impossible to combine the two real sets.

We need to remove the variable defining the combined list because using `.union()` creates a new set if set up correctly (As shown in the [method table](2-set.md#common-set-methods) above). This leads us into our next problem: the pair have **.union()** set up like this: 

```python
8 # Combine the two sets into one
9 combined_set.union(even_number_set, odd_number_set)
```

They're trying to combine the two sets into the `combined_set` by placing them in the parameter slots of union method and putting `combined_set` in front of the union method. However, this is not the correct way to do this. They need to set the `combined_set` variable to the new set created by the union. A correct way to implement this is: 


### **Jim & Jet's Needed Solution:**

```python
1 # Create the odd and even sets
2 even_number_set = {0, 2, 4, 6, 10}
3 odd_number_set = {1, 3, 5, 7, 9}
4 
5
6 # ...We removed the unneeded combined_set variable. 
7
5 # Combine the two sets into one
6 combined_set = even_number_set.union(odd_number_set) # a correct implementation of union
7 
8 # Print the resulting set.
9 print(combined_set)
```
>
> {0, 1, 2, 3, 4, 5, 6, 7, 9, 10}
>

> Download [2-guided_activity_solution.py](python_files/2-guided_activity_solution.py)

With this new solution, both `.union()` and `set()` are implemented correctly. When you work with sets in the future, make sure to use the right data type and format the union method the correct way.

---

### 2. A Chaotic College Picnic (Individual Activity)

The local college planned a day at the park with different activities, people, and food. You were tasked to find people who wanted to participate in these activities. You make sure to mention that if they do come, they'll get free food. When the time came to start the picnic however, it's a mess. People don't show up, activities don't go to plan, and you need to think of a solution fast. You need to find a way to use all the **default** set methods to complete the exercise.  Below is this problem represented with sets.

> **Download Problem:** [2-individual_activity_problem.py](python_files/2-individual_activity_problem.py)

**Objective:** Create organized sets as described in the **above** document by doing the following:

**Guidance:**

+ **Follow Instructions:** Go through the **4 problems** given to solve in the activity above.
+ **Think Simple:** All the solutions to the problems are simple, and **example uses are in this lesson**.

**Challenge Yourself:**

Try to solve the problem on your own. Once completed or if you can't find a solution after **1 hour**, compare your solution with mine to see how they compare.

> **Download Solution:** [2-individual_activity_solution.py](python_files\2-individual_activity_solution.py)

## Conclusion
That's it! Once you feel comfortable with your understanding of **sets**, you can move onto my other lessons on [queues](1-queue.md) or [trees](3-tree.md).

## Contact
Comments or questions are welcome! Please feel free to contact me through my [school email](mailto:han22047@byui.edu).

This is my final project for CSE 212 or Programming w/ Data Structures. This is a course taught at BYU-I.

© 2024 Kaden Hansen. All Rights Reserved.