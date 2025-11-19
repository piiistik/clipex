from abc import ABC, abstractmethod
from typing import List


class CommandRunner(ABC):
    @abstractmethod
    def run(self, commands: List[str]) -> List[float]: ...
