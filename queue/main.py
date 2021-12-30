# Queue Scratchpad
# YOUR NAME
# Use this as a "scratchpad" to tinker with your queue.

from queue import Queue


# Example
q = Queue()
q.enqueue('fee')
q.enqueue('fi')
print('first', q.data.first.value)
print('last', q.data.last.value)
