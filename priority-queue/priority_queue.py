# PriorityQueue: An efficient priority queue.
# A binary heap does most of the work. Which leaves this implementation quite trivial.
# Passes all tests in test_priority_queue.py
# @author Julian Canepa

from job import Job
from max_heap import MaxHeap

class PriorityQueue:

    def __init__(self) -> None:
        self.heap = MaxHeap()

    def enqueue(self, job=Job) -> None:
        self.heap.insert(job)

    def dequeue(self):
        return self.heap.delete()

    def is_empty(self) -> bool:
        return self.heap._is_empty()