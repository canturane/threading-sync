import threading
import time
import random

# Question 1: Basic Counting Problem with Multiple Threads


def group_thread(group_no, student_count):
    print(f"Group {group_no}: {student_count} students were processed.")


def question1():
    total_students = 50
    group_count = 5
    students_per_group = total_students // group_count

    threads = []
    for i in range(group_count):
        t = threading.Thread(target=group_thread, args=(i + 1, students_per_group))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Each group has selected a representative.")


if __name__ == "__main__":
    print("Question 1: Basic Counting Problem with Multiple Threads")
    question1()
