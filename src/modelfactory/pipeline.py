from pathlib import Path
from typing import Self

from modelfactory.config.config_schemas import Config
from modelfactory.config.config_utils import load_config
from modelfactory.data import fingerprint, loader, splitter
from modelfactory.data.types import DataSplits


class Pipeline:
    def __init__(self, cfg: Config):
        self.cfg = cfg

    @classmethod
    def from_yaml(cls, path) -> Self:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"The file in the path {path} was not found")
        cfg = load_config(path)
        return cls(cfg)

    def run(self):
        data_cfg = self.cfg.data

        df = loader.load_csv(data_cfg)
        df_fingerprint = fingerprint.fingerprint_file(data_cfg.path)
        splits = DataSplits(
            **splitter.split_data(
                cfg_split=data_cfg.split,
                df=df,
                target=data_cfg.target,
                seed=self.cfg.seed,
            ),
            fingerprint=df_fingerprint,
            schema=fingerprint.describe_schema(df, data_cfg.target),
        )
        return splits
