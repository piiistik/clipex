from clipbench.experiment.experiment import Experiment
from clipbench.configuration.configuration import Configuration
from clipbench.core.evaluator import Evaluator
from clipbench.core.search_method.grid_sample import GridSearchMethod
from clipbench.core.command_runner.simple_runner import SimpleRunner

from clipbench.core.search_space import SearchSpace


class Executor:
    def __init__(self, configuration: Configuration):
        self._command_runner = SimpleRunner()
        self._search_method = GridSearchMethod()
        self._budget = configuration.budget

    def execute(self, experiment: Experiment) -> SearchSpace:
        search_space = {}
        evaluator = Evaluator(experiment, self._command_runner, search_space)
        self._search_method.run(experiment, search_space, evaluator, self._budget)

        return search_space
