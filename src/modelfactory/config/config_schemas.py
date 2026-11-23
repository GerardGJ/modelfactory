from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SplitConfig(StrictModel):
    test_size: float = Field(0.2, gt=0, lt=1)
    validation_size: float = Field(0.2, gt=0, lt=1)
    stratify: bool = True


class DataConfig(StrictModel):
    path: str
    target: str
    split: SplitConfig = SplitConfig()


class ModelConfig(StrictModel):
    type: str
    params: dict = {}


class MetricsConfig(StrictModel):
    primary: str
    additional: list[str] = []


class IntParam(StrictModel):
    type: Literal["int"]
    low: int
    high: int


class FloatParam(StrictModel):
    type: Literal["float"]
    low: float
    high: float
    log: bool = False


class TuningConfig(StrictModel):
    enabled: bool = False
    n_trials: int = Field(50, gt=0)
    direction: Literal["maximize", "minimize"] = "maximize"
    pruner: str | None = None
    search_space: dict[str , IntParam | FloatParam] = {}


class TrackingConfig(StrictModel):
    tracking_uri: str
    tags: dict = {}


class PromotionConfig(StrictModel):
    metric: str
    min_improvement: float


class RegistryConfig(StrictModel):
    register_best: bool = True
    model_name: str
    promotion: PromotionConfig 


class Config(StrictModel):
    project: str
    experiment: str
    seed: int = 42
    data: DataConfig
    model: ModelConfig
    metrics: MetricsConfig
    tuning: TuningConfig = TuningConfig()
    tracking: TrackingConfig
    registry: RegistryConfig
