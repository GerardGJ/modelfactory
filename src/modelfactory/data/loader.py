from pathlib import Path

import pandas as pd

from modelfactory.config.config_schemas import DataConfig


def load_csv(cfg: DataConfig) -> pd.DataFrame:
    path = Path(cfg.path)

    if path.exists():
        df = pd.read_csv(path, sep=cfg.separator)
        return df
    raise FileNotFoundError(f"The file in the path {path} was not found")
