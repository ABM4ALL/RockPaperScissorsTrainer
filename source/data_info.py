import sqlalchemy

from Melodie import DataFrameInfo

simulator_scenarios = DataFrameInfo(
    df_name="simulator_scenarios",
    file_name="SimulatorScenarios.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "run_num": sqlalchemy.Integer(),
        "period_num": sqlalchemy.Integer(),
        "agent_num": sqlalchemy.Integer(),
        "payoff_win_min": sqlalchemy.Float(),
        "payoff_win_max": sqlalchemy.Float(),
        "payoff_lose_min": sqlalchemy.Float(),
        "payoff_lose_max": sqlalchemy.Float(),
        "payoff_tie": sqlalchemy.Float(),
    },
)

trainer_scenarios = DataFrameInfo(
    df_name="trainer_scenarios",
    file_name="TrainerScenarios.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "period_num": sqlalchemy.Integer(),
        "agent_num": sqlalchemy.Integer(),
        "payoff_win_min": sqlalchemy.Float(),
        "payoff_win_max": sqlalchemy.Float(),
        "payoff_lose_min": sqlalchemy.Float(),
        "payoff_lose_max": sqlalchemy.Float(),
        "payoff_tie": sqlalchemy.Float(),
    },
)

trainer_params_scenarios = DataFrameInfo(
    df_name="trainer_params_scenarios",
    file_name="TrainerParamsScenarios.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "path_num": sqlalchemy.Integer(),
        "generation_num": sqlalchemy.Integer(),
        "strategy_population": sqlalchemy.Integer(),
        "mutation_prob": sqlalchemy.Float(),
        "strategy_param_code_length": sqlalchemy.Integer(),
        "strategy_param_1_min": sqlalchemy.Float(),
        "strategy_param_1_max": sqlalchemy.Float(),
        "strategy_param_2_min": sqlalchemy.Float(),
        "strategy_param_2_max": sqlalchemy.Float(),
        "strategy_param_3_min": sqlalchemy.Float(),
        "strategy_param_3_max": sqlalchemy.Float()
    },
)

agent_params = DataFrameInfo(
    df_name="Parameter_AgentParams",
    columns={
        "id_scenario": sqlalchemy.Integer(),
        "id": sqlalchemy.Integer(),
        "strategy_param_1": sqlalchemy.Float(),
        "strategy_param_2": sqlalchemy.Float(),
        "strategy_param_3": sqlalchemy.Float(),
    },
)
