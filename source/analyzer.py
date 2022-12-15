import os
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np

from Melodie import Config
from Melodie import db


class RPSAnalyzer:

    def __init__(self, config: "Config"):
        self.fig_folder = config.output_folder
        self.db = db.create_db_conn(config)

    def plot_training_process(
            self,
            id_trainer_scenario: int = 0,
            id_trainer_params_scenario: int = 0,
    ):
        trainer_params_scenarios = self.db.read_dataframe("trainer_params_scenarios")
        path_num = trainer_params_scenarios.at[id_trainer_scenario, "path_num"]
        df = self.db.read_dataframe("env_trainer_result_cov")
        df = df.loc[(df["id_trainer_scenario"] == id_trainer_scenario) &
                    (df["id_trainer_params_scenario"] == id_trainer_params_scenario)]
        payoff_paths = {}
        payoff_cov_paths = {}
        for id_path in range(0, path_num):
            df_path = df.loc[df["id_path"] == id_path]
            payoff_paths[f"path_{id_path + 1}"] = df_path["total_accumulated_payoff_mean"].to_numpy()
            payoff_cov_paths[f"path_{id_path + 1}"] = df_path["total_accumulated_payoff_cov"].to_numpy()

        self.plot_paths(
            paths=payoff_paths,
            fig_name=f"AccumulatedPayoff_TS{id_trainer_scenario}PS{id_trainer_params_scenario}",
            y_label="Accumulated Payoff",
            y_limit=(0, 100000)
        )
        self.plot_paths(
            paths=payoff_cov_paths,
            fig_name=f"AccumulatedPayoffCov_CS{id_trainer_scenario}PS{id_trainer_params_scenario}",
            y_label="Accumulated Payoff (Coefficient of Variance)",
            y_limit=(0, 0.5)
        )

    def plot_paths(self, paths: Dict[str, np.ndarray], fig_name: str, y_label: str = None,  y_limit: tuple = None):
        figure = plt.figure(figsize=(12, 6))
        ax = figure.add_axes((0.1, 0.1, 0.8, 0.8))
        if y_limit:
            ax.set_ylim(y_limit)
        ax.set_xlabel("Generation", fontsize=15)
        if y_label:
            ax.set_ylabel(y_label, fontsize=15)
        x = [i for i in range(0, len(list(paths.values())[0]))]
        for id_path, values in paths.items():
            ax.plot(x, values, label=id_path)
        ax.legend(fontsize=12)
        self.save_fig(figure, fig_name)

    def save_fig(self, fig, fig_name):
        fig.savefig(
            os.path.join(self.fig_folder, fig_name + ".png"),
            dpi=200,
            format="PNG",
        )
        plt.close(fig)


