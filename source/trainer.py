from Melodie import Trainer
from source.agent import RPSAgent


class RPSTrainer(Trainer):

    def setup(self):
        self.add_agent_training_property(
            "agents",
            [
                "strategy_param_1",
                "strategy_param_2",
                "strategy_param_3"
            ],
            lambda scenario: list(range(scenario.agent_num)),
        )

    def collect_data(self):
        self.add_agent_property("agents", "strategy_param_1")
        self.add_agent_property("agents", "strategy_param_2")
        self.add_agent_property("agents", "strategy_param_3")
        self.add_environment_property("total_accumulated_payoff")

    def utility(self, agent: RPSAgent):
        return agent.accumulated_payoff
