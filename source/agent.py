import random
from typing import TYPE_CHECKING

from Melodie import Agent

if TYPE_CHECKING:
    from source.scenario import RPSScenario


class RPSAgent(Agent):
    scenario: "RPSScenario"

    def setup(self):
        self.payoff_rock_win: float = 0.0
        self.payoff_rock_lose: float = 0.0
        self.payoff_paper_win: float = 0.0
        self.payoff_paper_lose: float = 0.0
        self.payoff_scissors_win: float = 0.0
        self.payoff_scissors_lose: float = 0.0
        self.payoff_tie: float = 0.0
        self.strategy_param_1: float = 0.0
        self.strategy_param_2: float = 0.0
        self.strategy_param_3: float = 0.0
        self.setup_agent_vars()

    def setup_agent_vars(self):
        self.id_competitor: int = 0
        self.action: str = ""
        self.result: str = ""
        self.payoff: float = 0.0
        self.accumulated_payoff: float = 0.0
        self.n_rock: int = 0
        self.n_paper: int = 0
        self.n_scissors: int = 0
        self.share_rock: float = 0
        self.share_paper: float = 0
        self.share_scissors: float = 0

    def setup_action_prob(self):
        if self.strategy_param_1 == self.strategy_param_2 == self.strategy_param_3 == 0:
            self.strategy_param_1 = self.strategy_param_2 = self.strategy_param_3 = 1
        weight_sum = self.strategy_param_1 + self.strategy_param_2 + self.strategy_param_3
        self.action_prob = {
            "rock": self.strategy_param_1 / weight_sum,
            "paper": self.strategy_param_2 / weight_sum,
            "scissors": self.strategy_param_3 / weight_sum,
        }

    def setup_action_payoff(self):
        self.action_payoff = {
            ("rock", "win"): self.payoff_rock_win,
            ("rock", "lose"): self.payoff_rock_lose,
            ("paper", "win"): self.payoff_paper_win,
            ("paper", "lose"): self.payoff_paper_lose,
            ("scissors", "win"): self.payoff_scissors_win,
            ("scissors", "lose"): self.payoff_scissors_lose,
            ("rock", "tie"): self.payoff_tie,
            ("paper", "tie"): self.payoff_tie,
            ("scissors", "tie"): self.payoff_tie,
        }

    def select_action(self):
        rand = random.uniform(0, 1)
        if rand <= self.action_prob["rock"]:
            self.action = "rock"
            self.n_rock += 1
        elif self.action_prob["rock"] < rand <= self.action_prob["rock"] + self.action_prob["paper"]:
            self.action = "paper"
            self.n_paper += 1
        else:
            self.action = "scissors"
            self.n_scissors += 1

    def set_action_payoff(self):
        self.payoff = self.action_payoff[(self.action, self.result)]
        self.accumulated_payoff += self.payoff

    def calc_action_percentage(self):
        self.share_rock = self.n_rock / self.scenario.period_num
        self.share_paper = self.n_paper / self.scenario.period_num
        self.share_scissors = self.n_scissors / self.scenario.period_num





















