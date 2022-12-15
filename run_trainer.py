from source.scenario import RPSScenario
from source.model import RPSModel
from source.trainer import RPSTrainer
from config import config
from source.data_loader import RPSDataLoader


if __name__ == "__main__":
    trainer = RPSTrainer(
        config=config,
        scenario_cls=RPSScenario,
        model_cls=RPSModel,
        data_loader_cls=RPSDataLoader,
        # processors=4
    )
    trainer.run()
