# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Passes all tests in test_naive_priority_queue.py
# @author Julian Canepa

class NaivePriorityQueue:
    def __init__(self) -> None:
        self.data = []

    def enqueue(self, job):
        self.data.append(job)

    def dequeue(self):
        if self.is_empty():
            return None

        job = self.data[0]

        for el in self.data:
            if el >= job:
                job = el
        self.data.remove(job)

        return job

    def is_empty(self) -> bool:
        return len(self.data) == 0