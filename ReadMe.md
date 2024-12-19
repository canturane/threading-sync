# Threading and Synchronization in Python

This project demonstrates threading concepts and synchronization mechanisms using Python. Two scenarios are covered:

1. **Basic Counting Problem with Multiple Threads (Question 1)**
2. **Canteen Queue Synchronization Using Semaphores (Question 2)**

## Table of Contents
- [Threading and Synchronization in Python](#threading-and-synchronization-in-python)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Question 1: Basic Counting Problem](#question-1-basic-counting-problem)
    - [Description](#description)
    - [Key Features](#key-features)
    - [Code Walkthrough](#code-walkthrough)
    - [Output Example](#output-example)
  - [Question 2: Canteen Queue Synchronization](#question-2-canteen-queue-synchronization)
    - [Description](#description-1)
    - [Key Features](#key-features-1)
    - [Code Walkthrough](#code-walkthrough-1)
    - [Output Example](#output-example-1)
  - [Concepts Used](#concepts-used)
  - [How to Run](#how-to-run)
  - [License](#license)

---

## Overview
This project showcases the use of Python’s `threading` module for handling multi-threaded tasks. Each scenario addresses real-world problems involving thread management and synchronization:

1. **Question 1** simulates dividing students into groups and processing them in parallel.
2. **Question 2** models a canteen system where students queue up for food, and semaphores control the capacity at each counter.

---

## Setup
### Prerequisites
- Python 3.6 or higher.
- A basic understanding of threading and synchronization in Python.

### Installation
1. Clone this repository:
   ```bash
   git clone 
   cd threading-sync
   ```
2. Ensure Python is installed:
   ```bash
   python --version
   ```
3. Run the code directly; no additional libraries are required.

---

## Question 1: Basic Counting Problem
### Description
In this problem, 50 students are divided into 5 groups, each containing 10 students. The task is to process all groups in parallel using threads. Once processed, each group selects a representative.

### Key Features
- **Threading:** Each group is processed by a separate thread.
- **Parallel Execution:** Threads run concurrently to simulate parallel group processing.

### Code Walkthrough
- **Threads Creation:**
  A thread is created for each group using the `threading.Thread` class.
  ```python
  t = threading.Thread(target=group_thread, args=(i + 1, students_per_group))
  ```
- **Processing:**
  Each thread prints a message indicating the group’s progress:
  ```python
  print(f"Group {group_no}: {student_count} students were processed.")
  ```
- **Joining Threads:**
  The main thread waits for all group threads to finish using `t.join()`.

### Output Example
```
Group 1: 10 students were processed.
Group 2: 10 students were processed.
Group 3: 10 students were processed.
Group 4: 10 students were processed.
Group 5: 10 students were processed.
Each group has selected a representative.
```

---

## Question 2: Canteen Queue Synchronization
### Description
This problem models a canteen where 50 students queue up to receive food from 3 counters. Each counter can serve up to 5 students at a time. Semaphores are used to manage the capacity at each counter, and locks ensure thread-safe printing.

### Key Features
- **Semaphores:** Used to restrict access to counters, ensuring no more than 5 students are served simultaneously at each counter.
- **Locks:** Ensure orderly printing by preventing multiple threads from writing to the console at the same time.
- **Random Delays:** Simulate real-world variability in serving times.

### Code Walkthrough
- **Queue Management:**
  A global queue represents students waiting for food:
  ```python
  queue = [i + 1 for i in range(TOTAL_STUDENTS)]
  ```
- **Semaphore for Counters:**
  Each counter is initialized with a maximum capacity:
  ```python
  counter_semaphores = [threading.Semaphore(MAX_CAPACITY) for _ in range(TOTAL_COUNTERS)]
  ```
- **Serving Students:**
  Threads pop students from the queue and simulate serving:
  ```python
  student = queue.pop(0)
  print(f"Counter {counter_no}: 1 student received food. Remaining students: {len(queue)}")
  ```
- **Waiting When Full:**
  Counters pause when capacity is full:
  ```python
  print(f"Counter {counter_no} is full, students are waiting.")
  ```

### Output Example
```
Counter 1: 1 student received food. Remaining students: 49
Counter 2: 1 student received food. Remaining students: 48
Counter 3: 1 student received food. Remaining students: 47
Counter 1: 1 student received food. Remaining students: 46
...
Counter 2 is full, students are waiting.
...
All students have been served. The program is ending.
```

---

## Concepts Used
1. **Threading:** Enables concurrent execution of tasks.
2. **Semaphores:** Manage access to shared resources (e.g., counters in Question 2).
3. **Locks:** Prevent race conditions by synchronizing shared resource access.
4. **Random Delays:** Simulate realistic time variability in operations.

---

## How to Run
1. Ensure you are in the project directory.
2. Run the program for Question 1:
   ```bash
   python question1.py
   ```
3. Run the program for Question 2:
   ```bash
   python question2.py
   ```

---

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

For any questions or feedback, please reach out to [your-email@example.com].

