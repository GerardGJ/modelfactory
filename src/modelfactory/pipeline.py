from config.config_utils import load_config
from config.config_schemas import Config

class Pipeline():
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def run(self):
        pass