import pandas as pd
from pathlib import Path
import logging
from scripts.logging_config import setup_logging

#Logging settings, ignore it bruv
setup_logging()

#Path to the cleaned files

def load(df_cleaned : pd.DataFrame, filename = "Default_clean.txt", data_dir = None):
    
    #Check if our data_dir was passed correctly:
    if data_dir == None:
        data_dir = Path(__file__).parent.parent / "data" / "clean"
    
    #Clarify where we put the data
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    data_path = data_dir / filename
    
    #See if the file with that name already exists there
    if data_path.exists():
        logging.error(f"File with the name {filename} already exists in the {data_dir}, overwriting it right now...")
        df_cleaned.to_csv(data_path, index=False)
    #If it doesn't then we put it there
    else:
        df_cleaned.to_csv(data_path, index = False)
        logging.info(f"Successfully loaded the cleaned file into the {data_dir} directory, its name is {filename}")