import abc
import functools

class AbstractExpensiveCalculator(abc.ABC):
    @functools.cached_property
    @abc.abstractmethod
    def calculate(self):
        pass

AbstractExpensiveCalculator()