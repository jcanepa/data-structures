# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_naive_priority_queue

import unittest
import time
from naive_priority_queue import NaivePriorityQueue
from job import Job

class TestNaivePriorityQueue(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A NaivePriorityQueue exists.
        """
        try:
            NaivePriorityQueue()
        except NameError:
            self.fail("Could not instantiate NaivePriorityQueue.")

    def test_internal(self):
        """
        A NaivePriorityQueue uses a list to store its data.
        """
        pq = NaivePriorityQueue()
        self.assertEqual(list, type(pq.data))

    def test_enqueue_one_internal(self):
        """
        Enqueueing a value adds it to the internal list.
        """
        pq = NaivePriorityQueue()
        j = Job(5, 'The')
        pq.enqueue(j)
        self.assertEqual(j, pq.data[0])

    def test_enqueue_two_internal(self):
        """
        Enqueueing two values results in the first enqueued value being the first
        one in the list, and the second value being the last one in the list.
        """
        pq = NaivePriorityQueue()
        first = Job(5, 'new')
        second = Job(6, 'moon')
        pq.enqueue(first)
        pq.enqueue(second)
        self.assertEqual(first, pq.data[0])
        self.assertEqual(second, pq.data[1])

    def test_enqueue_three_internal(self):
        """
        Enqueueing three values results in the first enqueued value being the first
        one in the list, and the third value being the last one in the list.
        """
        pq = NaivePriorityQueue()
        first = Job(5, 'rode')
        second = Job(6, 'high')
        third = Job(7, 'in')
        pq.enqueue(first)
        pq.enqueue(second)
        pq.enqueue(third)
        self.assertEqual(first, pq.data[0])
        self.assertEqual(second, pq.data[1])
        self.assertEqual(third, pq.data[2])

    def test_dequeue_one(self):
        """
        Dequeuing from a single-element queue returns the single value.
        """
        pq = NaivePriorityQueue()
        j = Job(5, 'the')
        pq.enqueue(j)
        self.assertEqual(j, pq.dequeue())

    def test_dequeue_one_internal(self):
        """
        Dequeuing from a single-element queue removes it from the internal list.
        """
        pq = NaivePriorityQueue()
        job = Job(5, 'crown')
        pq.enqueue(job)
        self.assertEqual(1, len(pq.data))
        _ = pq.dequeue()
        self.assertEqual(0, len(pq.data))

    # # Hint: NaivePriorityQueues perform a linear search. Don't optimize.

    def test_dequeue_two(self):
        """
        Dequeuing from a two-element queue returns the one with highest priority.
        """
        pq = NaivePriorityQueue()
        lower_priority = Job(1, 'of')
        higher_priority = Job(3, 'the')
        pq.enqueue(higher_priority)
        pq.enqueue(lower_priority)
        self.assertEqual(higher_priority, pq.dequeue())

    def test_dequeue_two_internal(self):
        """
        Dequeuing from a two-element queue removes the job with the highest
        priority from the list.
        """
        pq = NaivePriorityQueue()
        lower_priority = Job(1, 'metropolis')
        higher_priority = Job(3, 'shining')
        pq.enqueue(higher_priority)
        pq.enqueue(lower_priority)
        _ = pq.dequeue()
        self.assertEqual(lower_priority, pq.data[0])
        self.assertEqual(1, len(pq.data))

    def test_dequeue_three(self):
        """
        Dequeuing from a three-element queue returns the jobs with the highest
        priority.
        """
        pq = NaivePriorityQueue()
        lower_priority = Job(1, 'like')
        middle_priority = Job(3, 'who')
        higher_priority = Job(5, 'on')
        pq.enqueue(higher_priority)
        pq.enqueue(lower_priority)
        pq.enqueue(middle_priority)
        self.assertEqual(higher_priority, pq.dequeue())
        self.assertEqual(middle_priority, pq.dequeue())
        self.assertEqual(lower_priority, pq.dequeue())

    def test_dequeue_three_internal(self):
        """
        Dequeuing from a three-element queue removes each dequeued value from
        the internal list, highest-priority first.
        """
        pq = NaivePriorityQueue()
        lower_priority = Job(1, 'top')
        middle_priority = Job(3, 'of')
        higher_priority = Job(5, 'this')
        pq.enqueue(higher_priority)
        pq.enqueue(lower_priority)
        pq.enqueue(middle_priority)
        _ = pq.dequeue()
        self.assertEqual(lower_priority, pq.data[0])
        _ = pq.dequeue()
        self.assertEqual(lower_priority, pq.data[0])

    """
    Emptiness
    """

    def test_empty(self):
        """
        A queue is initially empty.
        """
        pq = NaivePriorityQueue()
        self.assertTrue(pq.is_empty())

    def test_not_empty(self):
        """
        A queue with one enqueued value is not empty.
        """
        pq = NaivePriorityQueue()
        pq.enqueue(Job(1, 'People'))
        self.assertFalse(pq.is_empty())

    def test_empty_after_dequeue(self):
        """
        A queue with one enqueued value is empty after dequeuing.
        """
        pq = NaivePriorityQueue()
        pq.enqueue(Job(1, 'was'))
        _ = pq.dequeue()
        self.assertTrue(pq.is_empty())

    def test_not_empty_multiple(self):
        """
        A queue with two enqueued values is not empty after dequeuing only one.
        """
        pq = NaivePriorityQueue()
        pq.enqueue(Job(1, 'hustling'))
        pq.enqueue(Job(3, 'arguing and bustling'))
        _ = pq.dequeue()
        self.assertFalse(pq.is_empty())

    def test_initial_dequeue(self):
        """
        Dequeuing from an empty queue returns None.
        """
        pq = NaivePriorityQueue()
        self.assertIsNone(pq.dequeue())

    """
    Algorithmic complexity
    """

    def test_enqueue_efficiency(self):
        """
        Enqueing a value is always O(1).
        """
        time_samples = []
        for _ in range(0, 1000):
            pq = NaivePriorityQueue()
            start_time = time.time()
            pq.enqueue('fake')
            end_time = time.time()
            time_samples.append(end_time - start_time)
        small_average_enqueue_time = sum(time_samples) / float(len(time_samples))

        large_queue = NaivePriorityQueue()
        for _ in range(0, 1000000):
            large_queue.enqueue('fake')
        large_time_samples = []
        for _ in range(0, 1000):
            start_time = time.time()
            large_queue.enqueue('fake')
            end_time = time.time()
            large_time_samples.append(end_time - start_time)
        large_average_enqueue_time = sum(large_time_samples) / float(len(large_time_samples))
        self.assertAlmostEqual(small_average_enqueue_time, large_average_enqueue_time, delta=small_average_enqueue_time)

    # While enqueing naively is efficient... what is the complexity of dequeuing?

    def test_dequeue_efficiency(self):
        """
        Dequeuing a value is O(n).
        """
        print("This test will take a while...") # See the comment below.
        time_samples = []
        for _ in range(0, 1000):
            pq = NaivePriorityQueue()
            pq.enqueue('fake')
            start_time = time.time()
            pq.dequeue()
            end_time = time.time()
            time_samples.append(end_time - start_time)
        small_average_dequeue_time = sum(time_samples) / float(len(time_samples))

        large_queue = NaivePriorityQueue()
        for _ in range(0, 1000000):
            large_queue.enqueue('fake')
        large_time_samples = []
        for _ in range(0, 1000):
            start_time = time.time()
            large_queue.dequeue()
            end_time = time.time()
            large_time_samples.append(end_time - start_time)
        large_average_dequeue_time = sum(large_time_samples) / float(len(large_time_samples))
        self.assertNotAlmostEqual(small_average_dequeue_time, large_average_dequeue_time, delta=small_average_dequeue_time)

    # Notice how the last test takes time to "prove."
    # By studying *algorithm analysis*, you can prove the efficiency deductively,
    # with formal proofs, rather than with long-running tests.


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
