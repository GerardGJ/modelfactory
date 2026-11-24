import hashlib

import pandas as pd


def fingerprint_file(path: str, algorithm="sha256") -> str:
    with open(path, "rb") as f:
        return hashlib.file_digest(f, algorithm).hexdigest()


def describe_schema(df: pd.DataFrame, target: str) -> dict:
    return {
        "n_rows": len(df),
        "n_cols": df.shape[1],
        "target": target,
        "columns": {col: str(dtype) for col, dtype in df.dtypes.items()},
    }
