from pathlib import Path

import yaml

from modelfactory.config.config_schemas import Config


def load_config(path: str) -> Config:
    path = Path(path)
    if path.exists():
        with open(path) as f:
            raw = yaml.safe_load(f)
        return Config.model_validate(raw)
    raise FileNotFoundError(f"The file in the path {path} was not found")
