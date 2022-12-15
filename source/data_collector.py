from Melodie import DataCollector


class RPSDataCollector(DataCollector):
    def setup(self):
        self.add_agent_property("agents", "id_competitor")
        self.add_agent_property("agents", "action")
        self.add_agent_property("agents", "result")
        self.add_agent_property("agents", "payoff")
        self.add_agent_property("agents", "accumulated_payoff")
        self.add_environment_property("total_accumulated_payoff")
