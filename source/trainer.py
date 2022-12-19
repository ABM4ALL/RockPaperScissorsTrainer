from Melodie import Trainer
from source.agent import RPSAgent


class RPSTrainer(Trainer):

    def setup(self):
        self.add_agent_training_property(
            container_name="agents",  # agent_list_name
            used_properties=[  # training_attributes
                "strategy_param_1",
                "strategy_param_2",
                "strategy_param_3"
            ],
            agent_ids=lambda scenario: list(range(scenario.agent_num)),  # necessary?
        )

    def collect_data(self):
        self.add_agent_property("agents", "strategy_param_1")
        self.add_agent_property("agents", "strategy_param_2")
        self.add_agent_property("agents", "strategy_param_3")
        self.add_agent_property("agents", "share_rock")
        self.add_agent_property("agents", "share_paper")
        self.add_agent_property("agents", "share_scissors")
        self.add_environment_property("total_accumulated_payoff")

    def utility(self, agent: RPSAgent):
        return agent.accumulated_payoff
