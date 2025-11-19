from typing import Tuple

TVariable = int | float


class Variable:
    def get_value_from_index(self, index: int) -> TVariable:
        pass

    def get_string_from_index(self, index: int) -> str:
        pass

    def get_index_range(self) -> Tuple[int, int]:
        pass
