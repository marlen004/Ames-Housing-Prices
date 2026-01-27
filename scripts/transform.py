import pandas as pd
import numpy as np
import logging
from scripts.logging_config import setup_logging
from pathlib import Path

#Logging settings, ignore it bruv
setup_logging()

def transform(df : pd.DataFrame) -> pd.DataFrame:
    print("Input shape:", df.shape)
    print("Input dtypes:\n", df.dtypes)
    print("\nFirst few rows:\n", df.head())
    
    df_copy = df.copy()
    
    #Separate numerical and categorical columns
    numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
    categorical_cols = df_copy.select_dtypes(exclude=[np.number]).columns
    
    #Clean the numerical ones
    for col in numeric_cols:
        #Fill the misssing values
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
        
        #Calculate mean, standard deviation
        mean = df_copy[col].mean()
        std = df_copy[col].std()
    
        #Set lower and upper limits for anomaly elimination
        lower_limit = mean - 3 * std
        upper_limit = mean + 3 * std
        
        #Erase anomalies
        df_copy[col] = df_copy[col].clip(lower = lower_limit, upper = upper_limit)
        
        #Keep the logs
        logging.info(f"Numerical column {col} successfully cleaned up")
        
    #Clean the categorical ones
    for col in categorical_cols:
        
        #Fill with the word Unknown
        df_copy[col] = df_copy[col].fillna("Unknown")
        
        #Keep logging my dawgling
        logging.info(f"A categorical column {col} successfully cleaned up")
    return df_copy
    