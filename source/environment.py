import random

from Melodie import AgentList
from Melodie import Environment

from source.agent import RPSAgent
from source.scenario import RPSScenario


class RPSEnvironment(Environment):
    scenario: "RPSScenario"

    def setup(self):
        self.total_accumulated_payoff = 0.0

    @staticmethod
    def agents_setup_data(agents: "AgentList[RPSAgent]"):
        for agent in agents:
            agent.setup_action_prob()
            agent.setup_action_payoff()

    def run_game_rounds(self, agents: "AgentList[RPSAgent]") -> None:
        assert self.scenario.agent_num % 2 == 0, "scenario.agent_num must be even number."
        agent_ids = [i for i in range(0, self.scenario.agent_num)]
        random.shuffle(agent_ids)
        while agent_ids:
            agent_1 = agents[agent_ids.pop()]
            agent_2 = agents[agent_ids.pop()]
            self.agents_battle(agent_1, agent_2)

    def agents_battle(self, agent_1: "RPSAgent", agent_2: "RPSAgent"):
        agent_1.id_competitor = agent_2.id
        agent_2.id_competitor = agent_1.id
        agent_1.select_action()
        agent_2.select_action()
        if agent_1.action == agent_2.action:
            agent_1.result = agent_2.result = "tie"
            agent_1.set_action_payoff()
            agent_2.set_action_payoff()
        else:
            if (agent_1.action == "rock" and agent_2.action == "paper") or \
               (agent_1.action == "paper" and agent_2.action == "scissors") or \
               (agent_1.action == "scissors" and agent_2.action == "rock"):
                agent_1.result = "lose"
                agent_2.result = "win"
                agent_1.set_action_payoff()
                agent_2.set_action_payoff()
            else:
                agent_1.result = "win"
                agent_2.result = "lose"
                agent_1.set_action_payoff()
                agent_2.set_action_payoff()
        self.total_accumulated_payoff += agent_1.payoff
        self.total_accumulated_payoff += agent_2.payoff


























