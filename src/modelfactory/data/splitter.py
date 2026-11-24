from pandas import DataFrame
from sklearn.model_selection import train_test_split

from modelfactory.config.config_schemas import SplitConfig


def split_data(cfg_split: SplitConfig, df: DataFrame, target: str, seed: int) -> dict:
    test_split = cfg_split.test_size
    val_split = cfg_split.validation_size
    stratify = cfg_split.stratify
    x = df.drop(columns=target)
    y = df[target]

    (x_train, x_test, y_train, y_test) = train_test_split(
        x, y, test_size=test_split, random_state=seed, stratify=y if stratify else None
    )

    x_train, x_val, y_train, y_val = train_test_split(
        x_train,
        y_train,
        test_size=val_split,
        random_state=seed,
        stratify=y_train if stratify else None,
    )

    return {
        "X_train": x_train,
        "y_train": y_train,
        "X_val": x_val,
        "y_val": y_val,
        "X_test": x_test,
        "y_test": y_test,
    }
