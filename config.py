import os

from Melodie import Config

config = Config(
    project_name="RockPaperScissorsTrainer",
    project_root=os.path.dirname(__file__),
    input_folder="data/input",
    output_folder="data/output",
)
