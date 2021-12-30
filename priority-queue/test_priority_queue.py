# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_priority_queue

import unittest
import time
import random
from priority_queue import PriorityQueue
from max_heap import MaxHeap
from job import Job

class TestPriorityQueue(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A PriorityQueue exists.
        """
        try:
            PriorityQueue()
        except NameError:
            self.fail("Could not instantiate PriorityQueue.")

    def test_internal(self):
        """
        A PriorityQueue uses a list to store its data.
        """
        pq = PriorityQueue()
        self.assertEqual(MaxHeap, type(pq.heap))

    """
    Enqueuing and dequeuing. A PriorityQueue is simple if you've got a binary heap.
    """

    def test_enqueue_dequeue_one(self):
        """
        Enqueueing a single value is immediately dequeable.
        """
        pq = PriorityQueue()
        j = Job(5, 'The')
        pq.enqueue(j)
        self.assertEqual(j, pq.dequeue())


    def test_enqueue_dequeue_two(self):
        """
        Dequeuing from a two-element queue returns the one with highest priority.
        """
        pq = PriorityQueue()
        lower_priority = Job(1, 'of')
        higher_priority = Job(3, 'the')
        pq.enqueue(higher_priority)
        pq.enqueue(lower_priority)
        self.assertEqual(higher_priority, pq.dequeue())
        pq = PriorityQueue()
        pq.enqueue(lower_priority)
        pq.enqueue(higher_priority)
        self.assertEqual(higher_priority, pq.dequeue())

    def test_enqueue_dequeue_three(self):
        """
        Dequeuing from a three-element queue returns the jobs with the highest
        priority.
        """
        pq = PriorityQueue()
        lower_priority = Job(1, 'like')
        middle_priority = Job(3, 'who')
        higher_priority = Job(5, 'on')
        pq.enqueue(higher_priority)
        pq.enqueue(lower_priority)
        pq.enqueue(middle_priority)
        self.assertEqual(higher_priority, pq.dequeue())
        self.assertEqual(middle_priority, pq.dequeue())
        self.assertEqual(lower_priority, pq.dequeue())

    """
    Emptiness
    """

    def test_empty(self):
        """
        A queue is initially empty.
        """
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())

    def test_not_empty(self):
        """
        A queue with one enqueued value is not empty.
        """
        pq = PriorityQueue()
        pq.enqueue(Job(1, 'People'))
        self.assertFalse(pq.is_empty())

    def test_empty_after_dequeue(self):
        """
        A queue with one enqueued value is empty after dequeuing.
        """
        pq = PriorityQueue()
        pq.enqueue(Job(1, 'was'))
        _ = pq.dequeue()
        self.assertTrue(pq.is_empty())

    def test_not_empty_multiple(self):
        """
        A queue with two enqueued values is not empty after dequeuing only one.
        """
        pq = PriorityQueue()
        pq.enqueue(Job(1, 'hustling'))
        pq.enqueue(Job(3, 'arguing and bustling'))
        _ = pq.dequeue()
        self.assertFalse(pq.is_empty())

    def test_initial_dequeue(self):
        """
        Dequeuing from an empty queue returns None.
        """
        pq = PriorityQueue()
        self.assertIsNone(pq.dequeue())

    """
    Final test.
    """

    def test_enqueue_dequeue_omg(self):
        """
        Dequeing from a big priority queue always returns the highest priority
        item that was in the queue.
        """
        pq = PriorityQueue()
        for _ in range(1000): # Add some zeroes for fun.
            pq.enqueue(Job(random.randint(1, 1000), "Escuchela, la ciudad respirando"))
        job = pq.dequeue()
        while not pq.is_empty():
            latest_job = pq.dequeue()
            self.assertTrue(job >= latest_job)
            job = latest_job


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
