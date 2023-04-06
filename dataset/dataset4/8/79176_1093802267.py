import abc
import functools

class AbstractExpensiveCalculator(abc.ABC):
    @abc.abstractmethod
    @functools.cached_property
    def calculate(self):
        pass

AbstractExpensiveCalculator()