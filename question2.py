import threading
import time
import random

# Constants
MAX_CAPACITY = 5
TOTAL_STUDENTS = 50
TOTAL_COUNTERS = 3

# Semaphores are created for each counter
counter_semaphores = [threading.Semaphore(MAX_CAPACITY) for _ in range(TOTAL_COUNTERS)]

# Students in the queue
queue = [i + 1 for i in range(TOTAL_STUDENTS)]

# Lock to prevent multiple threads from printing simultaneously
print_lock = threading.Lock()


def counter_thread(counter_no):
    global queue
    served_count = 0  # Number of students served at this counter

    while queue:
        counter_semaphores[counter_no].acquire()
        try:
            if queue:
                student = queue.pop(0)
                served_count += 1
                with print_lock:
                    print(
                        f"Counter {counter_no + 1}: 1 student received food. Remaining students: {len(queue)}"
                    )
                time.sleep(random.uniform(0.1, 0.3))  # Time to serve food
            if served_count >= MAX_CAPACITY:
                with print_lock:
                    print(f"Counter {counter_no + 1} is full, students are waiting.")
                time.sleep(random.uniform(0.1, 0.3))  # Waiting time
        finally:
            counter_semaphores[counter_no].release()

    with print_lock:
        print(f"Counter {counter_no + 1}: All students have been served.")


def question2():
    threads = []

    for i in range(TOTAL_COUNTERS):
        t = threading.Thread(target=counter_thread, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All students have been served. The program is ending.")


if __name__ == "__main__":
    print("Question 2: Canteen Queue Synchronization")
    question2()
