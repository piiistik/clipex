from dataclasses import dataclass

from clipex.experiment.line_definition import LineDefinition
from clipex.experiment.variable import VariableHolder


@dataclass
class Experiment:
    line_definition: LineDefinition
