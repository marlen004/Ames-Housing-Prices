from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load
from scripts.logging_config import setup_logging
import logging
from pathlib import Path
import pandas as pd
import numpy as np


#Logging setup
setup_logging()

#File URL and file name setup
file_url = "http://jse.amstat.org/v19n3/decock/AmesHousing.txt"
filename = "AmesHousing_raw.txt"

#Cleaned data directory setup
data_clean_dir = Path(__file__).parent / "data" / "clean"
data_clean_dir.mkdir(parents = True, exist_ok= True)

#Raw data directory setup
data_raw_dir = Path(__file__).parent / "data" / "raw"
data_raw_dir.mkdir(parents = True, exist_ok= True)

#If download(extract) fails we will get an exception and code will terminate
try:
    #Extract
    extract(file_url, "AmesHousing_raw.txt", data_raw_dir)
    logging.info(f"Extraction completed, saved at {data_raw_dir/"AmesHousing_raw.txt"}")
    
    #Get a pd.DataFrame
    df_raw = pd.read_csv(data_raw_dir/"AmesHousing_raw.txt", delimiter='\t')
    
    #Transform
    df_clean = transform(df_raw)
    logging.info(f"Transformation completed, currently a pd.DataFrame")
    
    #Load
    load(df_clean, "AmesHousing_clean.csv", data_clean_dir)
    logging.info(f"Loading completed, saved at {data_clean_dir/"AmesHousing_clean.csv"}")
    
except Exception as e:
    #Failed. Logging it
    print("Download probably failed, stopping the code")
    logging.error("Failed download, cannot continue, terminated")
    
    #To see where the error came from, we use traceback
    import traceback
    traceback.print_exc()
