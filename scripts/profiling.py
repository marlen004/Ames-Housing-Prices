import numpy as np
import pandas as pd
from pathlib import Path


def split_columns(df : pd.DataFrame) -> list:
    numericals = []
    categoricals = []
    for col in df.columns:
        if df[col].dtype == np.number:
            numericals.append(col)
        else:
            categoricals.append(col)
    return numericals, categoricals

def check_one_hot(df : pd.DataFrame) -> list:
    list = []
    for col in df.columns:
        if df[col].nunique() <= len(df) * 0.05:
            list.append(col)
    if list.count() == 0:
        return None
    else:
        return list

def check_normalize_straight(df : pd.DataFrame) -> list:
    list = []
    for col in df.columns:
        return list


def profile_data(data_dir = None):
    if data_dir == None:
        data_dir = Path(__file__).parent.parent / "data" / "raw"
    categorized = {""}
    return True
