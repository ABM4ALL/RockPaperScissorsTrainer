from typing import TYPE_CHECKING, Dict, Any

import numpy as np

from Melodie import DataLoader
from source import data_info

if TYPE_CHECKING:
    from source.scenario import RPSScenario


class RPSDataLoader(DataLoader):
    def setup(self):
        self.load_dataframe(data_info.simulator_scenarios)
        self.load_dataframe(data_info.trainer_scenarios)
        self.load_dataframe(data_info.trainer_params_scenarios)
        self.generate_agent_dataframe()

    @staticmethod
    def init_win_payoff(scenario: "RPSScenario"):
        return np.random.uniform(scenario.payoff_win_min, scenario.payoff_win_max)

    @staticmethod
    def init_lose_payoff(scenario: "RPSScenario"):
        return np.random.uniform(scenario.payoff_lose_min, scenario.payoff_lose_max)

    def generate_agent_dataframe(self):
        with self.dataframe_generator(
            data_info.agent_params, lambda scenario: scenario.agent_num
        ) as g:

            def generator_func(scenario: "RPSScenario") -> Dict[str, Any]:
                return {
                    "id": g.increment(),
                    "payoff_rock_win": self.init_win_payoff(scenario),
                    "payoff_rock_lose": self.init_lose_payoff(scenario),
                    "payoff_paper_win": self.init_win_payoff(scenario),
                    "payoff_paper_lose": self.init_lose_payoff(scenario),
                    "payoff_scissors_win": self.init_win_payoff(scenario),
                    "payoff_scissors_lose": self.init_lose_payoff(scenario),
                    "payoff_tie": scenario.payoff_tie,
                    "strategy_param_1": np.random.uniform(0, 100),
                    "strategy_param_2": np.random.uniform(0, 100),
                    "strategy_param_3": np.random.uniform(0, 100),
                }

            g.set_row_generator(generator_func)
