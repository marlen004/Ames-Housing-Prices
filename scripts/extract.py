import requests
from pathlib import Path
import pandas as pd
import logging
from scripts.logging_config import setup_logging

#Logging settings, ignore it bruv
setup_logging()

#The loader function for use in the main.py
def extract(file_url, filename = "Default name.txt", data_dir = None):
    
    #Check if our data_dir was passed correctly
    if data_dir == None:
        data_dir = Path(__file__).parent.parent / "data" / "raw"
        
    #Make sure we have a correct file structure in mind
    data_dir.mkdir(parents=True, exist_ok=True)
    data_path = data_dir / filename
    
    #Check if we already have the file
    if data_path.exists():
        logging.info(f"Found the {filename} file")
        print(f"File {data_path} already exists")
        return True
    #Else we download it
    else:
        logging.warning(f"File not found, downloading it from the {file_url} with the name {filename} at {data_dir}")
        #Try to get it by url
        try:
            response = requests.get(file_url)
            data_path.write_bytes(response.content)
            logging.info(f"Downloaded the file successfully, {filename} is now stored in {data_dir}")
            return True
        #If not, log why it failed
        except Exception as e:
            logging.error(f"Got the following exception: {e}")
            print(f"Raised an exception: {e}")
            return False



