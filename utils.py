import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def handle_missing_values(df, strategy='mean'):
    """
    Handle missing values in a DataFrame.

    Parameters:
    - df: pandas DataFrame
    - strategy: strategy for handling missing values ('mean', 'median', 'mode', 'drop')

    Returns:
    - df: pandas DataFrame with missing values handled
    """
    if strategy == 'mean':
        df.fillna(df.mean(), inplace=True)
    elif strategy == 'median':
        df.fillna(df.median(), inplace=True)
    elif strategy == 'mode':
        df.fillna(df.mode().iloc[0], inplace=True)
    elif strategy == 'drop':
        df.dropna(inplace=True)
    return df


def normalize_numerical_columns(df, columns):
    """
    Normalize specified numerical columns in a DataFrame.

    Parameters:
    - df: pandas DataFrame
    - columns: list of numerical columns to normalize

    Returns:
    - df: pandas DataFrame with specified columns normalized
    """
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def label_encode_categorical_columns(df, columns):
    """
    Label encode specified categorical columns in a DataFrame.

    Parameters:
    - df: pandas DataFrame
    - columns: list of categorical columns to label encode

    Returns:
    - df: pandas DataFrame with specified columns label encoded
    """
    le = LabelEncoder()
    df[columns] = df[columns].apply(lambda col: le.fit_transform(col))
    return df
