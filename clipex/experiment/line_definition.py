from typing import List, Dict, Tuple

from clipex.experiment.variable import Variable


VariableStr = str
VariablePosition = int


class LineDefinition:
    __line_template: List[str | VariableStr] = []
    __variable_map: Dict[VariablePosition, Variable] = {}

    def __init__(
        self,
        line_template: List[str | VariableStr] = None,
        variable_map: Dict[VariablePosition, Variable] = None,
    ):
        self.__line_template = line_template
        self.__variable_map = variable_map

    def get_line(self, variables: Dict[VariablePosition, int]) -> str:
        for position, indexed_value in variables.items():
            self.__set_variable(position, indexed_value)

        return "".join(self.__line_template)

    def get_variable_ranges(self) -> Dict[VariablePosition, Tuple[int, int]]:
        ranges = {}
        for position, variable in self.__variable_map.items():
            ranges[position] = variable.get_index_range()
        return ranges

    def __set_variable(self, position: VariablePosition, indexed_value: int):
        variable = self.__variable_map.get(position)
        if variable is None:
            raise ValueError(f"No variable found at line position {position}")

        self.__line_template[position] = variable.get_string_from_index(indexed_value)


class LineDefinitionBuilder:
    __line_template: List[str | VariableStr] = []
    __variable_map: Dict[VariablePosition, Variable] = {}

    def add_static_part(self, static_part: str):
        self.__line_template.append(static_part)

    def add_variable(self, variable: Variable):
        position = len(self.__line_template)
        self.__line_template.append("")
        self.__variable_map[position] = variable

    def build(self) -> LineDefinition:
        line_definition = LineDefinition(self.__line_template, self.__variable_map)
        return line_definition
