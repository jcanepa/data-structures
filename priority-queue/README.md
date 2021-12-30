[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6307246&assignment_repo_type=AssignmentRepo)
# You Don't Know Priority Queues (nor Binary Heaps)

But after this, you will.

In this assignment, you will engage in a test-driven development process to
implement a priority queue. We'll call it a "PriorityQueue." To get there, you'll
also implement another data structure: a binary max-heap we'll call "MaxHeap."

## Run the Test Suite

This project has four classes (Job, NaivePriorityQueue, MaxHeap and PriorityQueue)
and their corresponding tests. Run each one in this order, until each passes:

`python3 -m unittest test_job`

`python3 -m unittest test_naive_priority_queue`

`python3 -m unittest test_max_heap`

`python3 -m unittest test_priority_queue`

Open each pair of test and corresponding implementation files (eg *test_priority_queue.py* and *priority_queue.py*) in your editor of choice. Modify the implementations to pass their first test. After each test passes, create a commit. Then, uncomment the next test, and re-run the test suite. Implement what's necessary to pass the test, and then repeat this process.

**But wait!**

Toward the middle of the test suite, you should be thinking about the algorithmic efficiency of each operation. What should be O(1)? What should be logarithmic? In addition, try to implement your operations using recursion, whenever possible.

## Best Done in Pairs!

Get together with a friend in front of just one machine, and take turns being the driver. Change drivers after each test is passed. Don't forget to commit after each test.

(c) 2019 Yong Joseph Bakos. All rights reserved.
