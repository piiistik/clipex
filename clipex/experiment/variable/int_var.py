from typing import Tuple

from clipex.experiment.variable.variable import Variable


class IntVar(Variable):
    def __init__(self, range_from: int, range_to: int, step: int = 1):
        super().__init__()
        self._range_from = range_from
        self._range_to = range_to
        self._step = step

    def get_value_from_index(self, index: int) -> int:
        value = self._range_from + index * self._step
        if value > self._range_to:
            raise IndexError("Index out of range for IntVar")
        return value

    def get_string_from_index(self, index: int) -> str:
        return str(self.get_value_from_index(index))

    def get_index_range(self) -> Tuple[int, int]:
        count = ((self._range_to - self._range_from) // self._step) + 1
        return (0, count - 1)
