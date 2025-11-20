from typing import Tuple

from clipex.experiment.variable.variable import Variable


class FloatVar(Variable):
    def __init__(self, range_from: float, range_to: float, step: float = 1.0):
        super().__init__()
        self._range_from = range_from
        self._range_to = range_to
        self._step = step

    def get_value_from_index(self, index: int) -> float:
        value = self._range_from + index * self._step
        if value > self._range_to:
            raise IndexError("Index out of range for FloatVar")
        return value

    def get_string_from_index(self, index: int) -> str:
        return str(round(self.get_value_from_index(index), 2))

    def get_index_range(self) -> Tuple[int, int]:
        count = int(((self._range_to - self._range_from) / self._step)) + 1
        return (0, count - 1)
