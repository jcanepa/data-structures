# Job: A process or task that has a priority.
# Passes all tests in test_job.py
# @author Julian Canepa

class Job:
    def __init__(self, priority=None, message=None) -> None:
        self.priority = priority
        self.message = message

    def __eq__(self, o: object) -> bool:
        return self.priority == o.priority

    def __lt__(self, o: object) -> bool:
        return self.priority < o.priority

    def __le__(self, o: object) -> bool:
        return self.priority <= o.priority

    def __gt__(self, o: object) -> bool:
        return self.priority > o.priority

    def __ge__(self, o: object) -> bool:
        return self.priority >= o.priority

    def __repr__(self) -> str:
        return self.__class__.__name__ \
            +' '+ str(self.priority) \
            +': '+ self.message
