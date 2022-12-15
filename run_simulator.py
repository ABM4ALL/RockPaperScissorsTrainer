from Melodie import Simulator
from config import config
from source.data_loader import RPSDataLoader
from source.model import RPSModel
from source.scenario import RPSScenario

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=RPSModel,
        scenario_cls=RPSScenario,
        data_loader_cls=RPSDataLoader
    )
    simulator.run()
