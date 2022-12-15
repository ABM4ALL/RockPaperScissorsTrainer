from typing import TYPE_CHECKING

from Melodie import Model
from source import data_info
from source.agent import RPSAgent
from source.data_collector import RPSDataCollector
from source.environment import RPSEnvironment
from source.scenario import RPSScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class RPSModel(Model):
    scenario: "RPSScenario"

    def create(self):
        self.agents: "AgentList[RPSAgent]" = self.create_agent_list(RPSAgent)
        self.environment: "RPSEnvironment" = self.create_environment(RPSEnvironment)
        self.data_collector = self.create_data_collector(RPSDataCollector)

    def setup(self):
        self.agents.setup_agents(
            agents_num=self.scenario.agent_num,
            params_df=self.scenario.get_dataframe(data_info.agent_params),
        )

    def run(self):
        for period in range(0, self.scenario.period_num):
            self.environment.agents_setup_data(self.agents)
            self.environment.run_game_rounds(self.agents)
            self.environment.agents_calc_action_share(period, self.agents)
            self.data_collector.collect(period)
        self.data_collector.save()


