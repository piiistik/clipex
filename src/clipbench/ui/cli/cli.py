from clipbench.experiment_converter.experiment_provider import provide_experiment
from clipbench.result_viewer.result_viewer import plot_heatmap

from clipbench.configuration.configuration import Configuration
from clipbench.core.executor import Executor


def main():
    print("Hello from CLI 👋")

    experiment = provide_experiment("temp/input.xml")
    print(experiment.get_search_space_definition())
    
    configuration = Configuration(command_runner_configuration={"name": "simple_runner"}, search_method_configuration={"name": "grid_sample"}, budget=20)
    print(configuration)
    
    executor = Executor(configuration)
    searched = executor.execute(experiment)

    plot_heatmap(searched, "temp/result.jpg")


if __name__ == "__main__":
    main()
