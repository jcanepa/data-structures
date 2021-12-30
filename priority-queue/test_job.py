# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_job

import unittest
import time
from job import Job


class TestJob(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Job exists.
        """
        try:
            Job()
        except NameError:
            self.fail("Could not instantiate Job.")

    def test_default_attributes(self):
        """
        A default Job has a priority and message that are None.
        """
        j = Job()
        self.assertEqual(None, j.priority)
        self.assertEqual(None, j.message)

    def test_attributes(self):
        """
        A Job is instantiated with a priority and a message.
        """
        j = Job(23, "Fake message")
        self.assertEqual(23, j.priority)
        self.assertEqual("Fake message", j.message)

    """
    Comparisons. A larger priority value indicates a higher priority.
    Hint: Investigate how to override Python comparison operators.
    """

    def test_eq(self):
        """
        Jobs with equivalent priorities are equal to each other.
        """
        first = Job(1, "Fake message")
        second = Job(1, "Don't care about the message")
        third = Job(3, "Don't care about the message")
        self.assertTrue(first == second)
        self.assertTrue(second == first)
        self.assertFalse(first == third)
        self.assertFalse(second == third)

    def test_lt(self):
        """
        A Job with a smaller priority is 'less than' a job with a larger priority.
        """
        smaller = Job(1, "Fake message")
        larger = Job(10, "Fake message")
        self.assertTrue(smaller < larger)
        self.assertFalse(larger < smaller)

    def test_gt(self):
        """
        A Job with a larger priority is 'greater than' a job with a smaller priority.
        """
        larger = Job(10, "Fake message")
        smaller = Job(1, "Fake message")
        self.assertTrue(larger > smaller)
        self.assertFalse(smaller > larger)

    def test_le(self):
        """
        A Job with a smaller priority is 'less than or equal to' a job with an
        equal or larger priority.
        """
        smaller = Job(1, "Fake message")
        smaller2 = Job(1, "Fake message")
        larger = Job(10, "Fake message")
        self.assertTrue(smaller <= larger)
        self.assertFalse(larger <= smaller)
        self.assertTrue(smaller <= smaller2)
        self.assertFalse(larger <= smaller2)

    def test_ge(self):
        """
        A Job with a larger priority is 'greater than or equal to' a job with an
        equal or smaller priority.
        """
        larger = Job(10, "Fake message")
        larger2 = Job(10, "Fake message")
        smaller = Job(1, "Fake message")
        self.assertTrue(larger >= smaller)
        self.assertFalse(smaller >= larger)
        self.assertTrue(larger >= larger2)
        self.assertFalse(smaller >= larger2)

    """
    String representation. Might be handy later, but hopefully you won't need it.
    """

    def test_repr(self):
        """
        A job displays its priority and message when printed.
        Hint: Investigate __repr__.
        """
        j = Job(42, "Fake message one")
        self.assertEqual("Job 42: Fake message one", str(j))
        self.assertEqual("Job 42: Fake message one", repr(j))
        j = Job(76, "Fake message two")
        self.assertEqual("Job 76: Fake message two", str(j))
        self.assertEqual("Job 76: Fake message two", repr(j))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
